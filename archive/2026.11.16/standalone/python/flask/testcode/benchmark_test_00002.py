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


@app.route("/BenchmarkTest00002", methods=["POST"])
def BenchmarkTest00002():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parts = str(json_value).split(',')
    data = ' '.join(parts)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return jsonify({"result": "success"})
