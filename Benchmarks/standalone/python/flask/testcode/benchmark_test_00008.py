# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00008", methods=["POST"])
def BenchmarkTest00008():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    reader = make_reader(db_value)
    data = reader()
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    if result is None:
        return jsonify({'error': 'not found'}), 404
    value = result['name']
    return jsonify({'name': str(value)}), 200
