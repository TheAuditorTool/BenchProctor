# SPDX-License-Identifier: Apache-2.0
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms
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


@app.route("/BenchmarkTest00111", methods=["POST"])
def BenchmarkTest00111():
    origin_value = request.headers.get('Origin', '')
    pending = list(str(origin_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    algorithm = algorithms.ARC4(key)
    encryptor = Cipher(algorithm, mode=None).encryptor()
    ciphertext = encryptor.update(str(data).encode()) + encryptor.finalize()
    return jsonify({'length': len(ciphertext)}), 200
