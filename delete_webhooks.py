#!/usr/bin/env python3
"""Delete a webhook"""


import requests
import json

api_key = ''  # personal api key
webhook_id = ''  # id of webhook
url = 'https://api.clickup.com/api/v2/webhook/{}'.format(webhook_id)

headers = {
    'Content-Type': 'application/json',
    'Authorization': api_key
    }

data = requests.request("DELETE", url, headers=headers)
print(data.text)