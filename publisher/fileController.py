'''
Add data to logs/ 
Get last file from logs
etc

'''

print('fileController initialized...')

import json
from typing import List, Dict
from pathlib import Path
from datetime import date, datetime

def save_snapshot(data: List[dict]) -> Path:
    '''
    Saves FULL data as a json file and puts it in logs.
    
    :param data: Data from digestion.merge_inventory_value()
    :type data: List[dict]
    :return: Created path
    :rtype: Path | None
    '''
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    today_str = date.today().isoformat()  # YYYY-MM-DD
    file_path = logs_dir / f"{today_str}.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return file_path

def get_last_two_snapshots() -> Dict:
    """
    Gives two last log files from logs path.
    
    :return: Data about two last log files.
    :rtype: Dict["latest": tuple(), "previous": tuple()]
    """
    logs_dir = Path("logs")

    files_with_dates = []

    for file in logs_dir.glob("*.json"):
        try:
            file_date = datetime.strptime(file.stem, "%Y-%m-%d").date()
            files_with_dates.append((file_date, file))
        except ValueError:
            print('Please do not put socks in logs')
            pass

    if len(files_with_dates) < 2:
        print("Could not find two log files... ")
        return None

    files_with_dates.sort(key=lambda x: x[0])

    prev_date, prev_file = files_with_dates[-2]
    last_date, last_file = files_with_dates[-1]

    return {
        "latest": (last_date, last_file),
        "previous": (prev_date, prev_file)
    }