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


@app.route("/BenchmarkTest00046", methods=["POST"])
def BenchmarkTest00046():
    origin_value = request.headers.get('Origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
