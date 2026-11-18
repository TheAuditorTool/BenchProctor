# SPDX-License-Identifier: Apache-2.0
import requests
from flask import Flask, jsonify
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00038", methods=["POST"])
def BenchmarkTest00038():
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    parts = []
    for token in str(api_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    db.execute("SELECT * FROM users WHERE id = '" + str(data) + "'")
    return jsonify({"result": "success"})
