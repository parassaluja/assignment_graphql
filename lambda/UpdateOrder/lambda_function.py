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
    db_table = "orders"

    args = event['arguments']['input']
    query = f"update {db_table} set userid = {args.get('userid')}, orderamount = {args.get('orderamount')}, orderdate = '{args.get('orderdate')}' where orderid = {args.get('orderid')}"
    queryget = f"select * from {db_table} where orderid = {args.get('orderid')}"

    print("**** query is :", query)

    conn = make_conn(db_name, db_user, db_host, db_pass)
    order_data = update_data(conn, query, queryget)

    return order_data


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
        data_dict = {'orderid': table_data[0], 'userid': table_data[1], 'orderamount': table_data[2],
                     'orderdate': str(table_data[3])}
    conn.commit()
    print("**** Data updated successfully ***** ")
    return data_dict


