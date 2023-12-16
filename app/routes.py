from app import app
from app.models import *
from app import save_webhook_output_file as file
from flask import request, jsonify
from app import basic_auth
import csv
import requests

# this webhook receives from the API

db = ''  # The database


@app.route('/')
def home():
    """To test the webhook activeness"""
    return 'Web hook is active. This is a protected resource\n', 200


@app.route('/webhook', methods=['POST', 'PUT'])
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
        # subtask = subTask()
        # subtask.id = id
        # subtask.name = name
        # db.save(subtask)
        # db.commit()
        with open(file, mode='a', newline='') as f:
            writer = csv.writer(f)
            if f.tell() == 0:
                writer.writerow(['id', 'name'])
            writer.writerow([id, name])
        return jsonify({'message': 'data saved succesfully'}), 200
    elif request.method == 'PUT':
        success = 0
        print('Webhook received')
        if request.is_json:
            task_info = request.get_json()
        else:
            task_info = request.form
        old_id = task_info.get('old_id')
        row_index = find_cell_indices(file, old_id)
        name = task_info.get('name')
        # subtask = subTask.query.filter_by(id=old_id).first()
        # if subtask:
        #     subtask.name = name
        #     db.save(subtask)
        #     db.commit()
        if row_index is not None:
            success = 1
            # the following code updates the csv file
            with open(file, 'r', newline='') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                rows[row_index]['name'] = name

            with open(file, 'w', newline='') as f:
                fieldnames = reader.fieldnames
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
        if success == 0:
            return jsonify({'message': f'task_id,  {old_id}, not found'}), 400
        return jsonify({'message': f'task_id,  {old_id}, modified \
succesfully'}), 200


def find_cell_indices(f, val):
    """This function finds the indices of the cell with the target value"""
    with open(f, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header row
        column_index = 0
        for row_index, row in enumerate(reader):
            if int(row[0]) == int(val):
                return row_index

    # Return None if the target value is not found
    return None
