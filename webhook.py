import requests
"""Create a webhook URL using POSTMAN for a collection"""

collection_name = 'ClickUp Public API'  # name of collection
api_key = ''  # api key for the POSTMAN API


def get_collection_uid(collection_name):
    """Get collection id from specified data"""
    url = 'https://api.getpostman.com/collections'
    headers = {'Content-Type': 'application/json', 'X-API-KEY': api_key}
    data = requests.get(url, headers=headers)
    data = data.json()
    for collection_info in data['collections']:
        if collection_info['name'] == collection_name:
            return collection_info['uid']
    return 'This collection does not exist'


def create_collection_webhook(collection_uid):
    """Creates collection webhook using the id"""
    url = 'https://api.getpostman.com/webhooks'
    headers = {'Content-Type': 'application/json', 'X-API-KEY': api_key}
    # running a POST request to the url
    webhook_name = 'ClickUp Webhook'  # random name for webhook
    data = {
        "webhook": {
            "name": webhook_name,
            "collection": collection_uid
            }
        }
    data = requests.post(url, headers=headers, json=data)
    data = data.json()
    info = {
        'name': data['webhook']['name'],
        'uid': data['webhook']['uid'],
        'id': data['webhook']['id'],
        'webhookUrl': data['webhook']['webhookUrl']
        }
    # returning the webhook url
    return info


collection_id = get_collection_uid(collection_name)
print(create_collection_webhook(collection_id))
