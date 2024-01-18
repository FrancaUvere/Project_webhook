#!/usr/bin/env python3
"""Edit the url of a webhook"""

import requests
import json

api_key = ''  # personal api key

webhook_id = ''  # id of webhook
url = 'https://api.clickup.com/api/v2/webhook/{}'.format(webhook_id)
headers = {
    'Content-Type': 'application/json',
    'Authorization': api_key
    }





payload = json.dumps({
    "endpoint": ''
    })
data = requests.request("PUT", url, headers=headers, data=payload)