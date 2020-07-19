# What are packages?

import pymysql
import argparse
import config

parser = argparse.ArgumentParser()
parser.add_argument('root_username')
parser.add_argument('root_password')

argp = parser.parse_args()

mysql_handle = pymysql.connect(
    host=config.db_host,
    port=3306,
    user=argp.root_username,
    password=argp.root_password,
    database='mysql'
)

for name, spec in config.db_setup.items():
    print(f'Setting up [{name}]')
    user = spec['user']
    password = config.get_password(user)
    database = spec['database']
    schema = spec['schema']

    with mysql_handle.cursor() as cursor:
        cursor.execute(f"DROP USER IF EXISTS '{user}'")
        cursor.execute(f"CREATE USER '{user}'@'%' IDENTIFIED BY '{password}'")
        cursor.execute(f"DROP DATABASE IF EXISTS {database}")
        cursor.execute(f"CREATE DATABASE {database}")
        cursor.execute(f"GRANT ALL ON {database}.* TO '{user}'@'%'")

    db_handle = pymysql.connect(
        host=config.db_host,
        port=3306,
        user=user,
        password=password,
        database=database
    )
    with db_handle.cursor() as cursor:
        for stmt in open(f"../db/{schema}").read().split(';'):
            if len(stmt.strip()) == 0: continue
            cursor.execute(stmt)
    db_handle.commit()
    db_handle.close()

mysql_handle.close()
