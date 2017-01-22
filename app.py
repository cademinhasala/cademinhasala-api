import os
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import redirect, request, url_for, Response
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
print os.environ['APP_SETTINGS']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#from models import Turma

@app.route("/")
def get_data():
#    with open(filename, "r") as f:
#        data = json.loads(f.read())
#    return Response(json.dumps(data), mimetype='application/json')
    return "teste"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=5003)
