# SPDX-License-Identifier: Apache-2.0
import random
from flask import Flask, request, jsonify
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00254", methods=["POST"])
def BenchmarkTest00254():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    token = random.randbytes(16).hex()
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return jsonify({'token': str(token)}), 200
