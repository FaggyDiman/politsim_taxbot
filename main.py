'''
Entry point for the workflow (master module)
'''

import parsers.dbFetcher
import parsers.currencyFetcher as getCurrency
import publisher.apiPublisher

getCurrency.get_html('https://politsim.ru/semenar_update_currency_rates_test.php')