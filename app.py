from flask import Flask, jsonify
import time

app = Flask(__name__)


@app.route("/")
def index():
    time.sleep(10)
    response = {"message": "Hello!"}
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(debug=True)
