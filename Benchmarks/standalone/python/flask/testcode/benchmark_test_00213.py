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


@app.route("/BenchmarkTest00213", methods=["POST"])
def BenchmarkTest00213():
    field_value = request.form.get('field', '')
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    padder = padding.PKCS7(128).padder()
    padded = padder.update(str(field_value).encode()) + padder.finalize()
    encryptor = Cipher(algorithms.AES(key), modes.ECB()).encryptor()
    ciphertext = encryptor.update(padded) + encryptor.finalize()
    return jsonify({'length': len(ciphertext)}), 200
