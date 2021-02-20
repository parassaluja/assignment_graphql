import json
import psycopg2
import traceback
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
    if event['source'] is None:
        args = event['arguments']
    else:
        args = event['source']
    if args.get('userid'):
        query = f"select * from orders where userid ={args.get('userid')}"
    else:
        query = f"select * from orders"

    print("**** query is :", query)
    conn = make_conn(db_name, db_user, db_host, db_pass)
    result = fetch_data(conn, query)
    print("**** result is :", result)

    return result


def make_conn(db_name, db_user, db_host, db_pass):
    conn = None
    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (db_name, db_user, db_host, db_pass))
    except:
        traceback.print_exc()
        print("I am unable to connect to the database")
    return conn


def fetch_data(conn, query):
    result = []
    cursor = conn.cursor()
    cursor.execute(query)
    for row in cursor:
        print(row)
        table_data = row
        data_dict = {'orderid': table_data[0], 'userid': table_data[1], 'orderamount': table_data[2],
                     'orderdate': str(table_data[3]) }
        result.append(data_dict)
    return result
