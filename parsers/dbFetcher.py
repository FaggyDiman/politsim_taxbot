'''
Fetches shop items from XF database
'''

import os

ab = os.getenv('DB_HOST')
if ab is not None:
    print('secret succesful')
else:
    print('Damn it')