# SPDX-License-Identifier: Apache-2.0
import json
import requests
from flask import Flask, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00043", methods=["POST"])
def BenchmarkTest00043():
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    data = api_value if api_value else 'default'
    parsed = json.loads(data)
    return jsonify({'parsed': str(parsed)}), 200
