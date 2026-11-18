# SPDX-License-Identifier: Apache-2.0
import os
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


@app.route("/BenchmarkTest00053", methods=["POST"])
def BenchmarkTest00053():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = json.loads(db_value).get('value', db_value)
    except (json.JSONDecodeError, AttributeError):
        data = db_value
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
