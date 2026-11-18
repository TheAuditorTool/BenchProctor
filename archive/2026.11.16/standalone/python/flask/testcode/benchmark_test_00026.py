# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from dataclasses import dataclass
from flask import Flask, request, jsonify
import os


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


@app.route("/BenchmarkTest00026", methods=["POST"])
def BenchmarkTest00026():
    user_id = request.args.get('id', '')
    form = FormData(payload=user_id)
    data = form.payload
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
