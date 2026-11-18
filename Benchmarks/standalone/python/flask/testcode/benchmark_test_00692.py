# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
import json
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00692", methods=["POST"])
def BenchmarkTest00692():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid number'}), 400
    processed = _coerced
    exec(str(processed))
    return jsonify({"result": "success"})
