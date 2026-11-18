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


@app.route("/BenchmarkTest00037", methods=["POST"])
def BenchmarkTest00037():
    auth_header = request.headers.get('Authorization', '')
    parts = str(auth_header).split(',')
    data = ' '.join(parts)
    try:
        _coerced = int(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    processed = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return jsonify({"result": "success"})
