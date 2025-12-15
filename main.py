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
    html = currencyFetcher.get_html('https://politsim.ru/semenar_update_currency_rates_test.php') #thx semen
    if html is None:
        raise RuntimeError(fancy_text)

    data = currencyFetcher.get_data(html) #getting every player's on hand money
    if data is None:
        raise RuntimeError(fancy_text)
    
    rates = currencyFetcher.get_currency_rates(html) #getting currency rates
    if rates is None:
        raise RuntimeError(fancy_text)

    print(rates)

    database = dbFetcher.connect_to_db(**credentials) #connecting to the database
    if database is None:
        raise RuntimeError(fancy_text)
    
    inventories = dbFetcher.fetch_inventories(database) #getting every player's inventory items
    if inventories is None:
        raise RuntimeError(fancy_text)
    
