from flask import Flask, jsonify

import logging

app = Flask(__name__)


FORMAT = "%(asctime)s, %(funcName)s %(message)s"

ENDPOINT_REACHED = "endpoint was reached"


@app.get("/")
def hello():
    app.logger.info(ENDPOINT_REACHED)
    return "Hello World!"


@app.get("/status")
def status():
    response = jsonify(user="admin", result="OK - healthy")
    app.logger.debug(ENDPOINT_REACHED)

    return response, 200


@app.get("/metrics")
def metrics():
    response = jsonify(
        status="success",
        code=0,
        data={"UserCount": 140, "UserCountActive": 23},
    )
    app.logger.debug(ENDPOINT_REACHED)

    return response, 200


if __name__ == "__main__":
    app.logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("app.log")
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)

    formatter = logging.Formatter(FORMAT)
    file_handler.setFormatter(formatter)

    app.run(host="0.0.0.0", debug=False)
