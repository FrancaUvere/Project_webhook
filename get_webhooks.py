import requests
import json


team_id = ''  # id of team
url = "https://api.clickup.com/api/v2/team/{}/webhook".format(team_id)

payload = ""
headers = {
  'Content-Type': 'application/json',
  'Authorization': '' # personal api key
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
