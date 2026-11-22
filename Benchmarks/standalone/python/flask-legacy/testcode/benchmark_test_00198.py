# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import Flask, jsonify
import json


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00198", methods=["POST"])
def BenchmarkTest00198():
    env_value = os.environ.get('APP_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
