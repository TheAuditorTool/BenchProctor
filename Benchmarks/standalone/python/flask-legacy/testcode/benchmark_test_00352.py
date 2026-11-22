# SPDX-License-Identifier: Apache-2.0
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from flask import Flask, request, jsonify
import os
import hashlib


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00352", methods=["POST"])
def BenchmarkTest00352():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    nonce = os.urandom(12)
    ciphertext = nonce + AESGCM(key).encrypt(nonce, str(data).encode(), None)
    return jsonify({'length': len(ciphertext)}), 200
