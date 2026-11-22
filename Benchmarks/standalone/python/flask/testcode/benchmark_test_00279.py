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


@app.route("/BenchmarkTest00279", methods=["POST"])
def BenchmarkTest00279():
    user_id = request.args.get('id', '')
    data = '%s' % str(user_id)
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    nonce = os.urandom(12)
    ciphertext = nonce + AESGCM(key).encrypt(nonce, str(data).encode(), None)
    return jsonify({'length': len(ciphertext)}), 200
