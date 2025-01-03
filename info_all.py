import requests
import time
import os
import re


headers = {
    'Connection': 'keep-alive',
    'Host': '127.0.0.1:13301',
    'Source-Type': '1',
    'client_session': 'YLCqDKwc7HzjrLRk+E7qQt8z+Iwhpb6UD22aIBW2dX0=',
    'info': 'vzfEEqkUjG|RymcKz9JmF',
    'sign': 'e4aea2eba51e1dfc5f582d9387c58f06',
    'userid': '14'
}



response = requests.get('http://127.0.0.1:13301/daily%2fwork%2fhis_consumer',headers=headers)

print(response.text)


