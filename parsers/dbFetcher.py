'''
Fetches value of inventories of players in XF database.
'''

import pymysql

print('dbFetcher initialized...')

def connect_to_db(host: str, user: str, password: str, database: str) -> pymysql.connect:
    connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=database,
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    if connection.open:
        print("Connection to the database established")
        return connection
    else:
        print("Couldn't connect to the database")
        return 0