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


@app.route("/BenchmarkTest00445", methods=["POST"])
def BenchmarkTest00445():
    multipart_value = request.form.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    processed = _bounded
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return jsonify({'allocated': allocated}), 200
