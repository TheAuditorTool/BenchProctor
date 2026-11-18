# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import requests
from flask import Flask, jsonify
import base64
import pickle


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00193", methods=["POST"])
def BenchmarkTest00193():
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    form = FormData(payload=api_value)
    data = form.payload
    pickle.loads(base64.b64decode(data))
    return jsonify({"result": "success"})
