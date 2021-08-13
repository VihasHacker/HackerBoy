import os
from flask import Flask
app = Flask('new tab
my_secret = os.environ['hfhgjkg']
')

@app.route('/')
def hello_world():
  return 'Hello, World!'

app.run(host='0.0.0.0', port=8080)