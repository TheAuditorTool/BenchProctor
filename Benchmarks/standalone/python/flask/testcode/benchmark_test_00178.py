# SPDX-License-Identifier: Apache-2.0
import numpy as np
from urllib.parse import unquote
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00178", methods=["POST"])
def BenchmarkTest00178():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    processed = _bounded
    quantity = int(processed)
    total_cents = np.int64(min(quantity, 100000)) * np.int64(1999)
    return jsonify({'total_cents': int(total_cents)}), 200
