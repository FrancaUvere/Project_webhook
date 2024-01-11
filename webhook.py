import requests
import json
"""Create a webhook URL using POSTMAN for a collection"""


collection_name = 'ClickUp Public API'  # name of collection
api_key = 'pk_62491440_N291XGYX67GC7D9OEAR0A03QG4PV119P'  # personal api key
ngrok_url = ' https://b88d-102-88-68-44.ngrok-free.app'

headers = {
    'Content-Type': 'application/json',
    'Authorization': api_key
    }

def create_collection_webhook(team_id, endpoint):
    """Creates collection webhook using the id"""
    url = "https://api.clickup.com/api/v2/team/{}/webhook".format(team_id)

    payload = json.dumps({
    "endpoint": "https://09a7-102-88-68-44.ngrok-free.ap/webhook",
    "events": [
        "taskCreated",
        "taskUpdated",
        "taskDeleted"
    ]
    })
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


data = create_collection_webhook('9015266874', ngrok_url)

print(data)



