from flask import Flask
from datetime import datetime
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/status")
def status():
    status=200
    user="admin"
    result="OK - healthy"
    app.logger.debug(f"{datetime.now()}, /status")
    return {"status": status,
            "user": user,
            "result":result,
            }

@app.route("/metrics")
def metrics():
    status = 200
    user = "admin"
    app.logger.debug(f"{datetime.now()}, /metrics")
    return {"status": status,
    "user":user,
    "data":{
        "UserCount": 140, "UserCountActive": 23,
    }
     }
    

if __name__ == "__main__":
    logging.basicConfig(filename="app.log",level=logging.DEBUG)
    app.run(host='0.0.0.0')
