# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import Flask, jsonify
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


@app.route("/BenchmarkTest00288", methods=["POST"])
def BenchmarkTest00288():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    form = FormData(payload=comment_value)
    data = form.payload
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    if result is None:
        return jsonify({'error': 'not found'}), 404
    value = result['name']
    return jsonify({'name': str(value)}), 200
