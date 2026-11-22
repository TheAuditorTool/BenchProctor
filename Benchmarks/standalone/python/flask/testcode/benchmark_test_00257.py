# SPDX-License-Identifier: Apache-2.0
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
from dataclasses import dataclass
from flask import Flask, jsonify
import os
import hashlib
from app_runtime import db


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


@app.route("/BenchmarkTest00257", methods=["POST"])
def BenchmarkTest00257():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    form = FormData(payload=db_value)
    data = form.payload
    key = hashlib.sha256(os.environ['DATA_ENC_KEY'].encode()).digest()
    nonce = os.urandom(12)
    ciphertext = nonce + ChaCha20Poly1305(key).encrypt(nonce, str(data).encode(), None)
    return jsonify({'length': len(ciphertext)}), 200
