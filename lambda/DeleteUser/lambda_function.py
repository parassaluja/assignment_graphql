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
    db_table = "users"

    args = event['arguments']['input']
    query = f"delete from {db_table} where userid = {args.get('userid')}"
    #queryget = f"select * from {db_table} where userid = {args.get('userid')}"

    print("**** query is :", query)

    conn = make_conn(db_name, db_user, db_host, db_pass)
    push_data(conn, query)

    return {
        "userid": args.get('userid')
    }


def make_conn(db_name, db_user, db_host, db_pass):
    conn = None
    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (db_name, db_user, db_host, db_pass))
    except:
        print("I am unable to connect to the database")
    return conn


def push_data(conn, query):

    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    print("**** Data inserted successfully ***** ")
    return





