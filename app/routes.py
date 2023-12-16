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
