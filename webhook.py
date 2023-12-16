from app import app
from app import save_webhook_output_file as file
from app.models import *
import csv


"""
This function retrieves the data from the csv file and saves to the database.
Import the function to the file where the database is configured
"""





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
