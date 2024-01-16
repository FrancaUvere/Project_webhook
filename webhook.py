import requests
import json
"""Create a webhook URL using POSTMAN for a collection"""


collection_name = 'ClickUp Public API'  # name of collection
api_key = ''  # personal api key
ngrok_url = ''

headers = {
    'Content-Type': 'application/json',
    'Authorization': api_key
    }

def create_collection_webhook(team_id, endpoint):
    """Creates collection webhook using the id"""
    url = "https://api.clickup.com/api/v2/team/{}/webhook".format(team_id)

    payload = json.dumps({
    "endpoint": endpoint,
    "events": [
        "taskCreated",
        "taskUpdated",
        "taskDeleted"
    ]
    })
    
    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text


data = create_collection_webhook(team_id, ngrok_url)

print(data)



