# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, jsonify
import json


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00291", methods=["POST"])
def BenchmarkTest00291():
    env_value = os.environ.get('APP_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid number'}), 400
    processed = _coerced
    code = compile(str(processed), '<rule>', 'exec')
    exec(code)
    return jsonify({"result": "success"})
