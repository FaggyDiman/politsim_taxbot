'''
Fetches value of inventories of players in XF database.
'''

import json
import pymysql
from collections import defaultdict, Counter

print('dbFetcher initialized...')

def connect_to_db(host: str, user: str, password: str, database: str) -> (pymysql.connect | None):
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
    
def fetch_inventories(connection: pymysql.connect) -> (list[dict] | None):
    """
    Returns a list with dictionaries in it:
    [{'user_id': 8, 62: 10, 39: 3}, ...]
    id of the item is key, quantity (occurences) of that item is value
    """
    result = []

    with connection.cursor() as cursor:
        cursor.execute("SELECT user_id, dbtech_shop_purchase FROM `xf_user`")
        rows = cursor.fetchall()

        for row in rows:
            user_id = row['user_id']
            blob_data = row['dbtech_shop_purchase']
            
            if not blob_data:
                continue

            try:
                json_data = json.loads(blob_data.decode('utf-8'))
            except Exception as e:
                print(f"Failed to decode JSON for user {user_id}: {e}")
                return None

            item_counter = Counter()
            for purchase in json_data.values():
                item_id = purchase.get('item_id')
                if item_id is not None:
                    item_counter[item_id] += 1

            user_dict = {'user_id': user_id}
            user_dict.update(dict(item_counter))
            result.append(user_dict)

    return result

