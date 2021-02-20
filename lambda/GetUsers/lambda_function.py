import json
import psycopg2
from conf import *


# import requests


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
    args = event['arguments']
    if args.get('userid'):
        query = f"select * from users where userid ={args.get('userid')}"
    else:
        query = f"select * from users"

    print("**** query is :", query)

    conn = make_conn(db_name, db_user, db_host, db_pass)
    users = fetch_data(conn, query)
    print("**** Users data is :", users)
    print("length is : ", len(users))
    if len(users) == 1:
        return users[0]
    else:
        return users

    # return {
    #     "userid": result['userid'],
    #     "name": result['name'],
    #     "age": result['age'],
    #     "email": result['email']
    # }


def make_conn(db_name, db_user, db_host, db_pass):
    conn = None
    try:
        conn = psycopg2.connect("dbname='%s' user='%s' host='%s' password='%s'" % (db_name, db_user, db_host, db_pass))
    except:
        print("I am unable to connect to the database")
    return conn


def fetch_data(conn, query):
    result = []
    print("Now executing: %s" % (query))
    cursor = conn.cursor()
    cursor.execute(query)
    # row = cursor.fetchall()
    for row in cursor:
        print(row)
        table_data = row
        data_dict = {}
        data_dict['userid'] = table_data[0]
        data_dict['name'] = table_data[1]
        data_dict['age'] = table_data[2]
        data_dict['email'] = table_data[3]
        result.append(data_dict)
    return result




