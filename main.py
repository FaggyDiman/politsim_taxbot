'''
Entry point for the workflow (master module)
'''

import parsers.dbFetcher
import parsers.currencyFetcher as getWealth
import publisher.apiPublisher


html = getWealth.get_html('https://politsim.ru/semenar_update_currency_rates_test.php')
print(getWealth.get_data(html))