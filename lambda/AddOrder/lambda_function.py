import json
import psycopg2
from conf import *


def lambda_handler(event, context):
    print(" ****** Event data is :", event)

    conf = Conf()
    param = conf.get_param()
    db_host = param["db_hostname"]
    db_port = 5432
    db_name = param["db_name"]
    db_user = param["db_user"]
    db_pass = param["db_pass"]
    db_table = "orders"

    args = event['arguments']['input']

    query = f"insert into {db_table} values ({args.get('orderid')}, {args.get('userid')}, {args.get('orderamount') }, '{args.get('orderdate')}')"

    queryget = f"select * from {db_table} where orderid = {args.get('orderid')}"

    print("**** query is :", query)

    conn = make_conn(db_name, db_user, db_host, db_pass)
    user_data = push_data(conn, query, queryget)

    return user_data


def make_conn(db_name, db_user, db_host, db_pass):
    conn = None
    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (db_name, db_user, db_host, db_pass))
    except:
        print("I am unable to connect to the database")
    return conn


def push_data(conn, query, queryget):

    cursor = conn.cursor()
    cursor.execute(query)
    cursor.execute(queryget)
    for row in cursor:
        print(row)
        table_data = row
        data_dict = {'orderid': table_data[0], 'userid': table_data[1], 'orderamount': table_data[2],
                     'orderdate': str(table_data[3])}
    conn.commit()
    print("**** Data inserted successfully ***** ")
    return data_dict





