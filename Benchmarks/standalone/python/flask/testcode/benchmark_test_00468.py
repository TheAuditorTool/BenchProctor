# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
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


@app.route("/BenchmarkTest00468", methods=["POST"])
def BenchmarkTest00468():
    header_value = request.headers.get('X-Custom-Header', '')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(header_value).encode())
    return jsonify({'length': len(ciphertext)}), 200
