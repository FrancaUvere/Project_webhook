To run the webhook:

- create ngrok account
- Install ngrok on the terminal 
- get you authentication code from ngrok account
- run 'ngrok config add-authtoken {your-auth-token}' to authenticate yoy ngrok
- run 'ngrok http 5000'

A temporary url is provied like:

Forwarding                    {ngrok-url} -> http://localhost:5000

- Copy the ngrok url and use it as the variable for ngrok_url in webhook.py
- input the values for the other required variable
  - run 'python3 create_subtasks.py'

This starts the webhook

Go ahead an create a task on your click up

Get back to your terminal and you'll see the details of the task created.


