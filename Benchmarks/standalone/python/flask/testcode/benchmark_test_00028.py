# SPDX-License-Identifier: Apache-2.0
from flask import Flask, current_app
from flask import request, jsonify
import json


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00028", methods=["POST"])
def BenchmarkTest00028():
    raw_body = request.get_data(as_text=True)
    try:
        data = json.loads(raw_body).get('value', raw_body)
    except (json.JSONDecodeError, AttributeError):
        data = raw_body
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid number'}), 400
    processed = _coerced
    current_app.config['ACTIVE_TENANT'] = str(processed)
    return jsonify({"result": "success"})
