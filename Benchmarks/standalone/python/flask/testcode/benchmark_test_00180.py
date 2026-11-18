# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import Flask, request, jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00180", methods=["POST"])
def BenchmarkTest00180():
    auth_header = request.headers.get('Authorization', '')
    form = FormData(payload=auth_header)
    data = form.payload
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid number'}), 400
    processed = _coerced
    eval(str(processed))
    return jsonify({"result": "success"})
