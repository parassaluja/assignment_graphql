import json
import psycopg2
import sys


# import requests


def lambda_handler(event, context):
    print(" ****** Event data is :", event)
    db_host = 'assignment-poc.csyzfnbq5xtf.ap-south-1.rds.amazonaws.com'
    db_port = 5432
    db_name = "assignmentdb"
    db_user = "postgres"
    db_pass = "paras123"
    db_table = "users"
    user_id = event['source']['userid']
    query = f"select * from orders where userid ={user_id}"
    # query = f"select * from orders"

    print("**** query is :", query)

    conn = make_conn(db_name, db_user, db_host, db_pass)
    result = fetch_data(conn, query)
    print("**** result is :", result)

    return result

    # return {
    #     "orderid" : result['orderid'],
    #     "userid" : result['userid'],
    #     "orderamount" : result['orderamount'],
    #     "orderdate" : result['orderdate']
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
        data_dict['orderid'] = table_data[0]
        data_dict['userid'] = table_data[1]
        data_dict['orderamount'] = table_data[2]
        data_dict['orderdate'] = str(table_data[3])
        result.append(data_dict)
    return result
