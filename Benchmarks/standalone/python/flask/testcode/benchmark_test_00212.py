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


@app.route("/BenchmarkTest00212", methods=["POST"])
def BenchmarkTest00212():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    plan_labels = {'basic': 'Basic plan', 'pro': 'Pro plan', 'team': 'Team plan'}
    label = plan_labels.get(str(data))
    if label is None:
        return jsonify({'error': 'unknown plan'}), 404
    value = label.upper()
    return jsonify({'plan': value}), 200
