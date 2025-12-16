'''
Publishing table as BB-code table for XF.
'''

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
    bb_template = f"""
[CENTER][B][FONT=Times New Roman][SIZE=22px]ФЕДЕРАЛЬНАЯ НАЛОГОВАЯ СЛУЖБА[/SIZE][/FONT][/B]
[FONT=Times New Roman][SIZE=22px]Автоматическая налоговая декларация[/SIZE][/FONT]
{prev_date} — {latest_date}[/CENTER]

[TABLE style='width: 100%;']
[TR]
[TD style='background-color: rgb(163, 143, 132);'][CENTER][B][FONT=Times New Roman]ГРАЖДАНИН[/FONT][/B][/CENTER][/TD]
[TD style='background-color: rgb(163, 143, 132);'][CENTER][B][FONT=Times New Roman]НАЛОГ (ЗОЛОТО)[/FONT][/B][/CENTER][/TD]
[TD style='background-color: rgb(163, 143, 132);'][CENTER][B][FONT=Times New Roman]НАЛОГ (МАРКИ)[/FONT][/B][/CENTER][/TD]
[/TR>
"""

    for entry in tax_list:
        user_str = f"[USER={entry['user_id']}]{entry['user_name']}[/USER]"
        gold_tax = entry['tax_base']
        currency_tax = entry['tax_currency']
        bb_template += f"[TR]\n[TD]{user_str}[/TD]\n[TD]{gold_tax}</TD>\n[TD]{currency_tax}[/TD]\n[/TR]\n"

    bb_template += "[/TABLE]"
    print('Message generated!')
    return bb_template