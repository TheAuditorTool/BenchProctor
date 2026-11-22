# SPDX-License-Identifier: Apache-2.0
from flask import Flask, current_app
import os
from flask import jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00035", methods=["POST"])
def BenchmarkTest00035():
    env_value = os.environ.get('APP_INPUT', '')
    pending = list(str(env_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid number'}), 400
    processed = _coerced
    current_app.config['ACTIVE_TENANT'] = str(processed)
    return jsonify({"result": "success"})
