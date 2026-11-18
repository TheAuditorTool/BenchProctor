# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, jsonify
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00384", methods=["POST"])
def BenchmarkTest00384():
    env_value = os.environ.get('APP_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return jsonify({'name': str(value)}), 200
