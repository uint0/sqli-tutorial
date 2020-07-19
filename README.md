# Sqli Tutorials

## Configuration
Configuration is controlled in two files; `config.py` controls database connection information, whilst
`levels.py` acts as configuration for each level.

### `config.py`
This file exposes 3 main symbols.
  - `get_password` should return the database password for a given user
  - `db_host` is the host on which the mysql database resides
  - `db_setup` exposes a list of known username, database, and schema file triplets
    - For a given setup
      - `user` is the username of a user with rights to access the database
      - `database` is the name of the database which holds the table for the given set of challenges
      - `schema` is a file containing the database schema

### `levels.py`
Levels contains the configurations for each level and group.
  - `groups` exposes all the groups in the tutorial. This should be an array of objects with the properties
    - `name`: Name of the group
    - `difficulty`: Brief flavor text describing the difficulty of the group
    - `flavor`: Flavor text for the group
    - `db`: An associated `db_setup` object from `config.py`
  - `levels` contains the specifications for each level, these contain 4 entries
    - `type`: What the type of the challenge is, this should be either `sql` or a string prefixed with `sqli-`
    - `group`: The index of the group this challenge belongs to (index in `groups`)
    - `name`: Name of the challenge
    - `spec`: A dictionary describing the specification of a challenge. See below for more

The bulk of this file lies in the `spec` field. This configures the challenge. The `type` field will inform
the program what type the `spec` is. Namely a `type=sql` spec will be handled differently to a `type=sqli` spec.

A `sql` spec should include
  - `question`: A one-line question prompt
  - `template`: A template for the sql that should be entered.
    - `{qN}` indicates blanks the user needs to fill in. `N` should be a `0` indexed increasing sequence
      - e.g. `SELECT {q0} FROM {q1} WHERE {q2}` will appear as `SELECT ___ FROM ___ WHERE ___`
  - `match`: A well-formed SQL query producing the expected result. This user's sql will be compared with the output of this query
    - Order matters
  - `flag`: A flag to give the user if their query matches the `match` query
  - `error-control`: One of `full`, `error`, or `blind`
    - `full` error control will return both the sql error message and the query that was execute back to the user
    - `error` error control will only return the sql error
    - `blind` error control will return no feedback

A `sqli` spec should include
  - `question`: same as `sql`
  - `show`: A dictionary containing an identifier followed by place holder text that should be shown to the user
    - e.g. `{'q0': 'Flag Id'}` will show a input with placeholder `Flag Id` to the user
       - Specifically at least the html `<input name="q0" placeholder="Flag Id">` will be generated
  - `template`: A sql query with `{identifier}`s corresponding to the identifiers in `show`. The user's inputs in `show` will be substituted here.
  - `match`: same as `sql`
  - `flag`: same as `sql`
  - `error-control`: same as `sql`

## Setup
Ensure mysql is running (on port 3306). Once `config.py` is appropriately setup,
simply invoking the following from within `/app` will setup all appropriate
users, databases, and schemas.

```
python3 _setup.py <root username> <root password>
```

## Running
The application can be run locally with the following from within `/app`. This will listen on port `5001`.
```
python3 app.py
```

Alternatively gunicorn can also be used to run the application. For production workloads `gunicorn` should be deployed with at least `gevent` or a reverse proxy.
