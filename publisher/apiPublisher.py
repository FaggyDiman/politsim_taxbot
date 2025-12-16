'''
Publishing table as BB-code table for XF.
'''

import requests

print('apiPublisher initialized...')

def generate_bbcode(tax_list, prev_date, latest_date) -> str: 
    '''
    :param tax_list: tax_list from taxCollector
    :param prev_date: prev_date from taxCollector
    :param latest_date: latest_date from taxCollector
    :return: BBcode msg to post onto a forum
    :rtype: str
    '''
    print('Generating message...')
    message = f"""
[CENTER][B][FONT=Times New Roman][SIZE=22px]ФЕДЕРАЛЬНАЯ НАЛОГОВАЯ СЛУЖБА[/SIZE][/FONT][/B]
[FONT=Times New Roman][SIZE=22px]Автоматическая налоговая декларация[/SIZE][/FONT]
{prev_date} — {latest_date}[/CENTER]

[TABLE style='width: 100%;']
[TR]
[TD style='background-color: rgb(163, 143, 132);'][CENTER][B][FONT=Times New Roman]ГРАЖДАНИН[/FONT][/B][/CENTER][/TD]
[TD style='background-color: rgb(163, 143, 132);'][CENTER][B][FONT=Times New Roman]НАЛОГ (ЗОЛОТО)[/FONT][/B][/CENTER][/TD]
[TD style='background-color: rgb(163, 143, 132);'][CENTER][B][FONT=Times New Roman]НАЛОГ (МАРКИ)[/FONT][/B][/CENTER][/TD]
[/TR]
"""

    for entry in tax_list:
        if entry['tax_base'] != 0.0:
            user_str = f"[USER={entry['user_id']}]{entry['user_name']}[/USER]"
            gold_tax = entry['tax_base']
            currency_tax = entry['tax_currency']
            message += f"[TR]\n[TD]{user_str}[/TD]\n[TD]{gold_tax}[/TD]\n[TD]{currency_tax}[/TD]\n[/TR]\n"

    message += "[/TABLE]"
    print('Message generated!')
    return message


def send_message(message: str, api_key: str, user_id: str, topic_id: str, api_url: str) -> (requests.Response | None):
    '''
    Sends a message via API key. 
    
    :param message: A message to post
    :type message: str
    :param api_key: API key
    :type api_key: str
    :param user_id: To post as unique user. Dunno how it works with a regular API key, I use a super one.
    :type user_id: str
    :param topic_id: Where you want to post the message
    :type topic_id: str
    '''
    print('Sending the message...')

    headers = {
        "XF-Api-Key": api_key,
        "XF-Api-User": user_id
    }
    params = {
        "thread_id": topic_id,
        "message": message
    }

    response = requests.post(api_url, headers=headers, params=params)

    if response.status_code == 200:
        print("The message was succesfuly sent!")
        return response
    else:
        print(f"Error occured while sending the message: {response.status_code} — {response.text}")
        return None


