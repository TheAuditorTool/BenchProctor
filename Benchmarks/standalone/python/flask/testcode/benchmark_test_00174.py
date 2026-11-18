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


@app.route("/BenchmarkTest00174", methods=["POST"])
def BenchmarkTest00174():
    ua_value = request.headers.get('User-Agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    try:
        _coerced = int(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    processed = _coerced
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return jsonify({"result": "success"})
