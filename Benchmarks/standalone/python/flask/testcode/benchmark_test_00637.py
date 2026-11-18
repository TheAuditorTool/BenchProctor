# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
from flask import Flask, jsonify
import os
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00637", methods=["POST"])
def BenchmarkTest00637():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    ciphertext = Fernet(os.environ['DATA_ENC_KEY'].encode()).encrypt(str(data).encode())
    return jsonify({'length': len(ciphertext)}), 200
