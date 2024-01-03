import requests
"""Create a webhook URL using POSTMAN for a collection"""

collection_name = 'ClickUp Public API'  # name of collection
api_key = ''  # api key for the POSTMAN API
workspace_name = '' #name of workspace


def get_collection_uid(collection_name):
    """Get collection id from specified data"""
    url = 'https://api.getpostman.com/collections'
    headers = {'Content-Type': 'application/json', 'X-API-KEY': api_key}
    data = requests.get(url, headers=headers)
    data = data.json()
    for collection_info in data['collections']:
        if collection_info['name'] == collection_name:
            return collection_info['uid']
    return None


def get_workspace_id(workspace_name):
    """Get workspace id from specified data"""
    url = 'https://api.getpostman.com/workspaces'
    headers = {'Content-Type': 'application/json', 'X-API-KEY': api_key}
    data = requests.get(url, headers=headers)
    data = data.json()
    for workspace_info in data['workspaces']:
        if workspace_info['name'] == workspace_name:
            return workspace_info['id']
    return None

def create_collection_webhook(collection_uid, workspace_id):
    """Creates collection webhook using the id"""
    url = 'https://api.getpostman.com/webhooks'

    #not including a 'workspace id' will create a webhook for the 'My workspace'
    params = {'workspace': workspace_id}
    headers = {'Content-Type': 'application/json', 'X-API-KEY': api_key}
    # running a POST request to the url
    webhook_name = 'ClickUp Webhook'  # random name for webhook
    data = {
        "webhook": {
            "name": webhook_name,
            "collection": collection_uid
            }
        }
    data = requests.post(url, headers=headers, params=params, json=data)
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
workspace_id = get_workspace_id(workspace_name)
print(create_collection_webhook(collection_id, workspace_id))
