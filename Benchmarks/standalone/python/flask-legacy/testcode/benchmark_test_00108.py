# SPDX-License-Identifier: Apache-2.0
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
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


@app.route("/BenchmarkTest00108", methods=["POST"])
def BenchmarkTest00108():
    raw_body = request.get_data(as_text=True)
    data = '%s' % str(raw_body)
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    padder = padding.PKCS7(128).padder()
    padded = padder.update(str(data).encode()) + padder.finalize()
    encryptor = Cipher(algorithms.AES(key), modes.ECB()).encryptor()
    ciphertext = encryptor.update(padded) + encryptor.finalize()
    return jsonify({'length': len(ciphertext)}), 200
