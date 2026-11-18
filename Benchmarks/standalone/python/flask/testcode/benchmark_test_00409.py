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


@app.route("/BenchmarkTest00409", methods=["POST"])
def BenchmarkTest00409():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ' '.join(parts)
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return jsonify({'name': str(value)}), 200
