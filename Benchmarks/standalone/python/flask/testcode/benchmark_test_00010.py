# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Flask, jsonify
import base64
import pickle


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00010", methods=["POST"])
def BenchmarkTest00010():
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    data = '{}'.format(api_value)
    pickle.loads(base64.b64decode(data))
    return jsonify({"result": "success"})
