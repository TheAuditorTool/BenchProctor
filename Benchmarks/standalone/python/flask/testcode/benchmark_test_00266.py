# SPDX-License-Identifier: Apache-2.0
import json
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


@app.route("/BenchmarkTest00266", methods=["POST"])
def BenchmarkTest00266():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    result = db.fetch_one('SELECT name FROM users WHERE id = ?', (str(data),))
    value = result['name']
    return jsonify({'name': str(value)}), 200
