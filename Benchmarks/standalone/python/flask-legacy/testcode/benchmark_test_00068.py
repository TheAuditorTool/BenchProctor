# SPDX-License-Identifier: Apache-2.0
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


@app.route("/BenchmarkTest00068", methods=["POST"])
def BenchmarkTest00068():
    user_id = request.args.get('id', '')
    data = RequestPayload(user_id).value
    try:
        _bounded = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    processed = _bounded
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return jsonify({'allocated': allocated}), 200
