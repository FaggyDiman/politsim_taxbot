'''
Entry point for the workflow (master module)
'''

import parsers.dbFetcher
import parsers.currencyFetcher as getWealth
import publisher.apiPublisher


html = getWealth.get_html('https://politsim.ru/semenar_update_currency_rates_test.php')
if html is not None:
    data = getWealth.get_data(html)
    if data is not None:
        pass
    else:
        raise RuntimeError('THE END...')
else:
    raise RuntimeError('THE END...')