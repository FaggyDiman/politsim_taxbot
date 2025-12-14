'''
Entry point for the workflow (master module)
'''

import os
from parsers import dbFetcher 
from parsers import currencyFetcher
import publisher.apiPublisher

fancy_text = 'Execution stopped'

credentials = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PSWD'),
    'database':os.getenv('DB_NAME')
    }

if __name__ == "__main__":
    html = currencyFetcher.get_html('https://politsim.ru/semenar_update_currency_rates_test.php')
    if html is None:
        raise RuntimeError(fancy_text)

    data = currencyFetcher.get_data(html)
    if data is None:
        raise RuntimeError(fancy_text)

    database = dbFetcher.connect_to_db(**credentials)
    if database is None:
        raise RuntimeError(fancy_text)
    
    inventories = dbFetcher.fetch_inventories(database)
    if inventories is None:
        raise RuntimeError(fancy_text)