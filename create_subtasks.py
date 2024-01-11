
from flask import Flask, request, jsonify
from ngrok_url import ngrok_url

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Handle the incoming webhook data
    webhook_data = request.json()
    print('Webhook Data:', webhook_data)

    # code for handling the webhook data goes here

    return jsonify({'message': 'Webhook received successfully'})

if __name__ == '__main__':
    app.run(debug=True)
