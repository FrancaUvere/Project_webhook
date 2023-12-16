from app import app
from app import save_webhook_output_file as file
from app.models import *
import csv


"""
This function retrieves the data from the csv file and saves to the database.
Import the function to the file where the database is configured
"""


def save_to_db(db):
    """Saves the data from the csv file to the database"""
    with open(file, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            subtask = subTask()
            subtask.id = row['id']
            subtask.name = row['name']
            db.save(subtask)
            db.commit()
    return True


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5443, debug=True)
