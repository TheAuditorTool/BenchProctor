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


@app.route("/BenchmarkTest00319", methods=["POST"])
def BenchmarkTest00319():
    host_value = request.headers.get('Host', '')
    kind = 'json' if str(host_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(host_value).strip()
        case _:
            data = str(host_value)
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    processed = _bounded
    count = int(processed)
    records = ctypes.create_string_buffer(min(count, 65536) * 64)
    return jsonify({'allocated': len(records)}), 200
