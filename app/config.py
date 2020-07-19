import os

def get_password(user):
    # TODO: support per user passwords
    return 'password'

db_host = os.getenv("MYSQL_HOST", "localhost")

db_setup = {
    'blog': {
        'user': 'blog',
        'database': 'blog',
        'schema': 'blogs.mysql.sql'
    },
    'video': {
        'user': 'video',
        'database': 'video',
        'schema': 'videos.mysql.sql'
    },
    'bank': {
        'user': 'bank',
        'database': 'bank',
        'schema': 'bank.mysql.sql'
    },
    'flag': {
        'user': 'flag',
        'database': 'flag',
        'schema': 'flags.mysql.sql'
    },
    'scenario': {
        'user': 'scenario',
        'database': 'scenario',
        'schema': 'scenarios.mysql.sql'
    },
}
