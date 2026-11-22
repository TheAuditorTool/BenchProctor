# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00032", methods=["POST"])
def BenchmarkTest00032():
    referer_value = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid number'}), 400
    processed = _coerced
    code = compile(str(processed), '<rule>', 'exec')
    exec(code)
    return jsonify({"result": "success"})
