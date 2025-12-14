'''
Entry point for the workflow (master module)
'''

import parsers.dbFetcher
import parsers.currencyFetcher as getCurrency
import publisher.apiPublisher


html = getCurrency.get_html('https://politsim.ru/semenar_update_currency_rates_test.php')
print(getCurrency.get_data(html))