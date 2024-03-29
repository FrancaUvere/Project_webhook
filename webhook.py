#!/usr/bin/env python3
from config import TEAM_ID
import requests
import json
"""Create a webhook URL using POSTMAN for a collection"""

collection_name = 'ClickUp Public API'  # name of collection
# api_key = 'pk_56513834_43ETQKCSOYGR2QOEWPRUGBYGTVFI1X2V'  # personal api key
api_key = 'pk_62446429_M1F4LVOEVU2G0M1RCXI2ER0LA52WIYOB'
ngrok_url = 'https://3631-102-88-71-171.ngrok-free.app'
# team_id = TEAM_ID
team_id = '9015247585'

headers = {
    'Content-Type': 'application/json',
    'Authorization': api_key
    }

def create_collection_webhook(team_id, endpoint):
    """Creates collection webhook using the id"""
    url = "https://api.clickup.com/api/v2/team/{}/webhook".format(team_id)

    payload = json.dumps({
    "endpoint": '{}/webhook'.format(endpoint),
    "events": [
        "taskCreated",
        "taskUpdated",
        "taskDeleted",
    ]
    })
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

data = create_collection_webhook(team_id, ngrok_url)

print(data)



