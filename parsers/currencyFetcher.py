'''
Fetches currency from Germany citizens.
'''

from typing import List
import requests
from bs4 import BeautifulSoup

print('currencyFetcher initialized...')

def get_html(url: str) -> str: #Getting url HTML raw txt
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'Successfully connected to {url}')
            return response.text
        else:   
            print(f'Failed to get {url}')
            return None
    except Exception as e:
        print('Error occured while trying to get HTML from {url}: {e.message}')
        return None

def get_data(html: str) -> List[dict]:
    pass