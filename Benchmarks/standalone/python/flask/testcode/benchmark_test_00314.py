# SPDX-License-Identifier: Apache-2.0
from cryptography.hazmat.decrepit.ciphers.algorithms import ARC4
from cryptography.hazmat.primitives.ciphers import Cipher
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


@app.route("/BenchmarkTest00314", methods=["POST"])
def BenchmarkTest00314():
    xml_value = request.get_data(as_text=True)
    if xml_value:
        data = xml_value
    else:
        data = ''
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    algorithm = ARC4(key)
    encryptor = Cipher(algorithm, mode=None).encryptor()
    ciphertext = encryptor.update(str(data).encode()) + encryptor.finalize()
    return jsonify({'length': len(ciphertext)}), 200
