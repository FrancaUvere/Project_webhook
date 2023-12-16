from app import app
from app.models import *
from app import save_webhook_output_file as file
from flask import request, jsonify
from app import basic_auth
import csv
import requests

# this webhook receives from the API


@app.route('/')
def home():
    """To test the webhook activeness"""
    return 'Web hook is active. This is a protected resource\n', 200


@app.route('/webhook', methods=['POST'])
@basic_auth.login_required
def webhook():
    """This receives the payload, stores the required information"""
    if request.method == 'POST':
        print('Webhook received')
        if request.is_json:
            task_info = request.get_json()
        else:
            task_info = request.form
        id = task_info.get('id')
        name = task_info.get('name')

        with open(file, mode='a', newline='') as f:
            writer = csv.writer(f)
            if f.tell() == 0:
                writer.writerow(['id', 'name'])
            writer.writerow([id, name])
        return jsonify({'message': 'data saved succesfully'}), 200
    else:
        print('Error webhook unreceived. Update unsuccesful'), 400


"""
The following code is for the API if it is needed to be queried.
In this situation, the webhoom database will not be updated in real time,
but will have to be run manually to update the database
"""


@app.route('/webhook_manual', methods=['POST'])
@basic_auth.login_required
def webhook_manual():
    """This receives the payload, stores the required information"""
    api_url = ''  # The API url
    headers = {}  # The headers for the API
    tasks = []  # The list of tasks
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        print('Webhook received')
        if request.is_json:
            task_infos = request.get_json()
        else:
            task_infos = request.form
        for task_info in task_infos:
            id = task_info.get('id')
            name = task_info.get('name')
            tasks.append([id, name])

        with open(file, mode='w', newline='') as f:
            writer = csv.writer(f)
            if f.tell() == 0:
                writer.writerow(['id', 'name'])
            for task in tasks:
                writer.writerow(task)
        return jsonify({'message': 'data saved succesfully'}), 200
    else:
        return jsonify({'message': 'Update unsuccesful'}), 400
