# SPDX-License-Identifier: Apache-2.0
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


@app.route("/BenchmarkTest00314", methods=["POST"])
def BenchmarkTest00314():
    origin_value = request.headers.get('Origin', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(origin_value),))
    if result is None:
        return jsonify({'error': 'not found'}), 404
    value = result['name']
    return jsonify({'name': str(value)}), 200
