import re
import flask
import pymysql
import config
from level import levels, groups

app = flask.Flask(__name__)

def get_schema(schema_file):
    schema = ''
    # TODO: don't get path traversalled
    with open(f"../db/{schema_file}") as f:
        schema = f.read().split('-- BEGIN PUBLIC')[1].split('-- END PUBLIC')[0].strip()
    return schema

def make_template(template):
    return re.sub(
        r"\{(q\d*)\}",
        lambda m: f'<input type="text" name="{m.group(1)}">',
        template
    )

def make_show(show_dict):
    return ''.join([
        f'<input type="text" name="{name}", placeholder="{placeholder}">'
        for name, placeholder in show_dict.items()
    ])

def query(sql, db=None, user=None):
    conn = pymysql.connect(
        host=config.db_host,
        user=user,
        password=config.get_password(user),
        db=db
    )
    with conn.cursor() as cursor:
        try:
            cursor.execute(sql)
            rv = (cursor.fetchall(), True)
        except Exception as e:
            rv = ([['Error', str(e)]], False)
    conn.close()
    return rv

def get_groups():
    hgroups = []
    for i, group in enumerate(groups):
        hgroups.append({
            'name': group['name'],
            'difficulty': group['difficulty'],
            'flavor': group['flavor'],
            'id': i,
            'levels': []
        })
    for i, level in enumerate(levels):
        hgroups[level['group']]['levels'].append({
            'id': i,
            'name': level['name']
        })
    return hgroups

def match_result(match, result):
    if len(match) != len(result):
        return False
    
    for i in range(len(match)):
        if len(match[i]) != len(result[i]):
            return False
        
        for j in range(len(result[i])):
            if result[i][j] != match[i][j]:
                return False
        
    return True

@app.route('/api/solve', methods=["POST"])
def x():
    challenge_id = flask.request.args.get('level', '')
    if challenge_id == '':
        return '', 400

    challenge = levels[int(challenge_id)]
    sql = challenge['spec']['template'].format(**flask.request.form.to_dict())
    group = groups[challenge['group']]
    db_spec = group['db']

    result, success = query(sql, db=db_spec['database'], user=db_spec['user'])
    match, _ = query(challenge['spec']['match'], db=db_spec['database'], user=db_spec['user'])

    if not success:
        if challenge['spec']['error-control'] == 'full':
            result += [['Query', sql]]
        elif challenge['spec']['error-control'] == 'error':
            result = result
        elif challenge['spec']['error-control'] == 'blind':
            result = []

    return flask.jsonify({
        'data': result,
        'message': challenge['spec']['flag'] if match_result(match, result) else False
    })

@app.route('/')
def index():
    challenge_id = flask.request.args.get('level', '')
    if challenge_id == '':
        return flask.render_template('index.html', groups=get_groups())

    challenge = levels[int(challenge_id)]
    group = groups[challenge['group']]
    if challenge['type'] == 'sql':
        return flask.render_template('sql.html',
            schema=get_schema(group['db']['schema']),
            title=group['name'],
            question=challenge['spec']['question'],
            template=make_template(challenge['spec']['template'])
        )
    elif challenge['type'].startswith('sqli'):
        return flask.render_template('sqli.html',
            schema=get_schema(group['db']['schema']),
            title=group['name'],
            question=challenge['spec']['question'],
            template=make_show(challenge['spec']['show'])
        ) 
    return flask.render_template('404.html')

if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0', debug=True)
