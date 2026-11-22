# SPDX-License-Identifier: Apache-2.0
import json
import os
from flask import Flask, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00237", methods=["POST"])
def BenchmarkTest00237():
    env_value = os.environ.get('APP_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    parsed = json.JSONDecoder().decode(str(data))
    return jsonify({'parsed': str(parsed)}), 200
