import os
import json
from flask import Flask
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 

app = Flask(__name__)

@app.route("/")
def get_data():
    return app.response_class(content_type='db.json')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5003)
