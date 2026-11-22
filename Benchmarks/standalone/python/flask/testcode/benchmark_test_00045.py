# SPDX-License-Identifier: Apache-2.0
import numpy as np
from flask import Flask, request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00045", methods=["POST"])
def BenchmarkTest00045():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = RequestPayload(graphql_var).value
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    processed = _bounded
    quantity = int(processed)
    total_cents = np.int64(min(quantity, 100000)) * np.int64(1999)
    return jsonify({'total_cents': int(total_cents)}), 200
