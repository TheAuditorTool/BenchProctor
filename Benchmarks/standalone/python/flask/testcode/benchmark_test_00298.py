# SPDX-License-Identifier: Apache-2.0
import ctypes
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00298", methods=["POST"])
def BenchmarkTest00298():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = ' '.join(str(forwarded_ip).split())
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    processed = _bounded
    count = int(processed)
    records = ctypes.create_string_buffer(min(count, 65536) * 64)
    return jsonify({'allocated': len(records)}), 200
