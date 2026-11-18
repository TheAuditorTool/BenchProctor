# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import base64
from flask import Flask, request, jsonify
import os


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00115", methods=["POST"])
def BenchmarkTest00115():
    cookie_value = request.cookies.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
