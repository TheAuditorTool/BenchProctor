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


@app.route("/BenchmarkTest00012", methods=["POST"])
def BenchmarkTest00012():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid number'}), 400
    processed = _coerced
    exec(str(processed))
    return jsonify({"result": "success"})
