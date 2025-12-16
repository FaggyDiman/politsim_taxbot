'''
Calculate tax using two json files from logs and metadata from fileController
'''

print('taxCollector initialized...')

import json
from pathlib import Path
from typing import Dict

def compute_tax(files_dict: dict, tax_rate: float, threshold: float, currency_rate: float = 1) -> Dict:
    latest_date, latest_file = files_dict["latest"]
    prev_date, prev_file = files_dict["previous"]

    with open(latest_file, "r", encoding="utf-8") as f:
        latest_data = json.load(f)

    with open(prev_file, "r", encoding="utf-8") as f:
        prev_data = json.load(f)

    prev_wealth_dict = {str(entry["user_id"]): entry["wealth"] for entry in prev_data}

    tax_list = []
    for entry in latest_data:
        user_id = str(entry["user_id"])
        latest_wealth = entry["wealth"]
        prev_wealth = prev_wealth_dict.get(user_id, 0.0) 

        wealth_diff = latest_wealth - prev_wealth
        tax = wealth_diff * tax_rate

        if tax < threshold * currency_rate:
            tax = 0.0

        tax_list.append({
            "user_id": user_id,
            "tax": round(tax, 2) 
        })

    return tax_list
