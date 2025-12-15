'''
Fetches wealth from Germany citizens as list[{user_id = int, wealth = float}, ...]
'''

from typing import List, Dict
import re
import requests
from bs4 import BeautifulSoup

print('currencyFetcher initialized...')

def get_html(url: str) -> (str | None): #Fetching url HTML raw txt
    print(f'Connecting...')
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f'Successfully connected to {url}')
            return response.text
        else:   
            print(f'Failed to get {url}')
            return None
    except Exception as e:
        print(f"Error occured while trying to get HTML from {url}: {e}")
        return None

def get_data(html: str) -> (List[dict] | None): #Getting list of dictionaries.
    '''
    Docstring for get_data
    
    :param html: html (probably parsed)
    :type html: str
    :return: list[{user_id = int, wealth = float}, ...]
    :rtype: List[dict] | None
    '''
    soup = BeautifulSoup(html, "html.parser")
    currency_p = soup.find("p", string=lambda t: t and "Идентификатор валюты: 3" in t)
    result = []

    if not currency_p:
        print('Currency header is not found')
        return None
    
    table = currency_p.find_next("table")
    if not table:
        print('Table is not found')
        return None
    
    rows = table.find_all("tr")[1:]
    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 2:
            continue
        link_text = cols[0].get_text()
        if "(#" in link_text:
            user_id = link_text.split("(#")[1].split(")")[0].strip()
            
        wealth = cols[1].get_text().strip()

        result.append({
            "user_id": user_id,
            "wealth": wealth
        })
    return result

def get_currency_rates(html: str) -> (Dict[str, float] | None):
    soup = BeautifulSoup(html, "html.parser")
    result: Dict[str, float] = {}

    currency_headers = soup.find_all(
        "p",
        string=re.compile(r"Идентификатор валюты:")
    )

    for header in currency_headers:
        header_text = header.get_text(strip=True)

        match = re.search(r"\(([^)]+)\)", header_text)
        if not match:
            continue

        currency = match.group(1)

        stats_block = header.find_next(
            "p",
            style=re.compile("padding-left")
        )
        if not stats_block:
            continue

        rate_label = stats_block.find(
            string=re.compile(r"Расчётный курс")
        )
        if not rate_label:
            continue

        rate_tag = rate_label.find_next("b")
        if not rate_tag:
            continue

        try:
            rate = float(rate_tag.get_text())
        except ValueError:
            print('An error occured when tried to get currency rates')
            return None
        
        result[currency] = rate

    return result