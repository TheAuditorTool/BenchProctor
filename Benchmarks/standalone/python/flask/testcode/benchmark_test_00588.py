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


@app.route("/BenchmarkTest00588", methods=["POST"])
def BenchmarkTest00588():
    raw_body = request.get_data(as_text=True)
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(raw_body), token))
    return jsonify({'token': str(token)}), 200
