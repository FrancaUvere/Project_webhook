
from flask import Flask, request, jsonify
import requests
from webhook import headers

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Handle the incoming webhook data
    webhook_data = request.get_json()
    for k, v in webhook_data.items():
        print(k, v, end='\n\n')

    parent_id = webhook_data['history_items'][0]['parent_id']
    task_id = webhook_data['task_id']

    print(parent_id, task_id)

    url = ''  # url for creating subtasks

    # uncomment these lines of code to create subtasks

    # data = {
    #     'parent_id': '',
    #     'task_id': '',
    # }
    # info = requests.post(url, json=data, headers=headers)
    # print(info.json())
   

    return jsonify({'message': 'Webhook received successfully'})

if __name__ == '__main__':
    app.run(debug=True)
