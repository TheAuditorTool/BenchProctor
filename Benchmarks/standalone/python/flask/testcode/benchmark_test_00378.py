# SPDX-License-Identifier: Apache-2.0
import secrets
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


@app.route("/BenchmarkTest00378", methods=["POST"])
def BenchmarkTest00378():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    parts = str(forwarded_ip).split(',')
    data = ' '.join(parts)
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return jsonify({'token': str(token)}), 200
