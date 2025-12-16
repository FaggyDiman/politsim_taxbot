'''
Digesting data fetched from currencyFetcher and dbFetcher. 
'''

import json
from typing import List, Dict

def merge_inventory_value(
    main_data: List[dict],
    inventories: tuple[dict],
    currency_rates: Dict[str, float],
    items_path: str = "items.json"
) -> List[dict]:
    """
    1) Calculates inventory value using currency rates
    2) Adds inventory value to main data
    3) Returns result in the format of main data

    :param main_data: Result of get_data()
    :param inventories: Result of fetch_inventories()
    :param currency_rates: Result of get_currency_rates()
    :param items_path: Path to items.json
    :return: Updated main_data: list[{user_id = int, wealth = float}, ...]
    """

    
    print('Calculating data...')

    # Load items data
    with open(items_path, "r", encoding="utf-8") as f:
        items_meta = json.load(f)

    inventory_by_user = {
        inv["user_id"]: inv["items"]
        for inv in inventories
    }

    for user in main_data:
        user_id = int(user["user_id"])
        inventory = inventory_by_user.get(user_id)

        total_inventory_value = 0.0

        if inventory:
            for item_id, quantity in inventory.items():
                item_key = str(item_id)

                if item_key not in items_meta:
                    continue

                item_info = items_meta[item_key]
                currency = item_info["type"]
                nominal_value = item_info["value"]

                rate = currency_rates.get(currency)
                if rate is None:
                    continue

                total_inventory_value += nominal_value * rate * quantity

        try:
            user["wealth"] = round(float(user["wealth"]) + total_inventory_value,2)
        except ValueError:
            user["wealth"] = round(total_inventory_value,2)

    return main_data
