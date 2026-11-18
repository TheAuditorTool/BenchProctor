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


@app.route("/BenchmarkTest00033", methods=["POST"])
def BenchmarkTest00033():
    referer_value = request.headers.get('Referer', '')
    form = FormData(payload=referer_value)
    data = form.payload
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid number'}), 400
    processed = _coerced
    exec(str(processed))
    return jsonify({"result": "success"})
