'''
Entry point for the workflow (master module)
'''

import parsers.dbFetcher
import parsers.currencyFetcher as getCurrency
import publisher.apiPublisher

getCurrency.get_html('ошибка')