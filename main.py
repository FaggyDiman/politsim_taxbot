'''
Entry point for the workflow (master module)
'''

import os
from parsers import dbFetcher 
from parsers import currencyFetcher
from parsers import digestion
from publisher import apiPublisher
from publisher import fileController
from publisher import taxCollector

THRESHOLD = 10
TAX_RATE = 0.08
API_KEY = os.getenv('API_KEY')
POSTER_ID = '2139'
DESTINATION = '7560'
API_URL = "https://politsim.ru/api/conversation-messages/"
DB_CREDENTIALS = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PSWD'),
    'database':os.getenv('DB_NAME')
    }

fancy_text = 'Execution stopped'




if __name__ == "__main__":


    html = currencyFetcher.get_html('https://politsim.ru/semenar_update_currency_rates_test.php') #thx semen
    if html is None:
        raise RuntimeError(fancy_text)

    on_hand_data = currencyFetcher.get_data(html) #getting every player's on hand money
    if on_hand_data is None:
        raise RuntimeError(fancy_text)
    
    rates = currencyFetcher.get_currency_rates(html) #getting currency rates
    if rates is None:
        raise RuntimeError(fancy_text)
    currency_rate = rates.get("mark")


    database = dbFetcher.connect_to_db(**DB_CREDENTIALS) #connecting to the database
    if database is None:
        raise RuntimeError(fancy_text)
    
    inventories = dbFetcher.fetch_inventories(database) #getting every player's inventory items
    if inventories is None:
        raise RuntimeError(fancy_text)
    
    full_data = digestion.merge_inventory_value(on_hand_data, inventories, rates) #merging data from db and semen's utilite
    if full_data is None:
        raise RuntimeError(fancy_text)
    
    fileController.save_snapshot(full_data)
    last_logs = fileController.get_last_two_snapshots() #get two last log files to compare them
    if last_logs is None:
        print("Can't proceed!")
    else:
        taxes, prev_date, latest_date = taxCollector.compute_tax(last_logs, TAX_RATE, THRESHOLD, currency_rate)
        message = apiPublisher.generate_bbcode(taxes, prev_date, latest_date)
        api_post = apiPublisher.send_message(message, API_KEY, POSTER_ID, DESTINATION, API_URL)
        if api_post is None:
            raise RuntimeError(fancy_text)
        print(api_post)

        
