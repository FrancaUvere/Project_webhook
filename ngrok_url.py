import subprocess
import time

def authenticate_ngrok(auth_token):
    # Set the authtoken for Ngrok
    ngrok_auth_cmd = f"ngrok authtoken {auth_token}"
    subprocess.run(ngrok_auth_cmd, shell=True)

def start_ngrok(port):
    # Start Ngrok to expose the local server
    ngrok_cmd = f"ngrok http {port}"
    ngrok_process = subprocess.Popen(ngrok_cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Give Ngrok some time to initialize
    time.sleep(5)

    # Extract Ngrok URL from the output
    ngrok_output = ngrok_process.stdout.read().decode('utf-8')
    ngrok_url = None
    for line in ngrok_output.split('\n'):
        if "Forwarding" in line:
            ngrok_url = line.split()[1]

    return ngrok_url


# Replace YOUR_AUTH_TOKEN and 5000 with your Ngrok authentication token and Flask app port
auth_token = "YOUR_AUTH_TOKEN"
app_port = 5000

# Authenticate Ngrok
authenticate_ngrok(auth_token)

# Start Ngrok and get the public URL
ngrok_url = start_ngrok(app_port)

if ngrok_url:
    print(f"Ngrok tunnel is live at: {ngrok_url}")
    # Now you can use ngrok_url as the webhook URL in Postman 
else:
    print("Failed to start Ngrok.")
