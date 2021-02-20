import json
import psycopg2
from conf import *


def lambda_handler(event, context):
    print(" ****** Event data is :", event)

    conf = Conf()
    param = conf.get_param()
    db_host = param["db_hostname"]
    db_name = param["db_name"]
    db_user = param["db_user"]
    db_pass = param["db_pass"]
    db_table = "users"

    args = event['arguments']['input']
    query = f"update {db_table} set name = '{args.get('name')}',age = {args.get('age')}, email = '{args.get('email')}' where userid = {args.get('userid')}"
    queryget = f"select * from {db_table} where userid = {args.get('userid')}"

    print("**** query is :", query)

    conn = make_conn(db_name, db_user, db_host, db_pass)
    user_data = update_data(conn, query, queryget)

    return user_data


def make_conn(db_name, db_user, db_host, db_pass):
    conn = None
    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (db_name, db_user, db_host, db_pass))
    except:
        print("I am unable to connect to the database")
    return conn


def update_data(conn, query, queryget):

    cursor = conn.cursor()
    cursor.execute(query)
    cursor.execute(queryget)
    for row in cursor:
        print(row)
        table_data = row
        data_dict = {'userid': table_data[0], 'name': table_data[1], 'age': table_data[2],
                     'email': str(table_data[3])}
    conn.commit()
    print("**** Data inserted successfully ***** ")
    return data_dict





