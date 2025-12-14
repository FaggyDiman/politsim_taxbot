'''
Fetches wealth from Germany citizens as list[{user_id = int, wealth = float}, ...]
'''

from typing import List
import requests
from bs4 import BeautifulSoup

print('currencyFetcher initialized...')

def get_html(url: str) -> (str | None): #Fetching url HTML raw txt
    print(f'Connecting to {url}...')
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