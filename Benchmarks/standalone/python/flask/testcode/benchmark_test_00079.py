# SPDX-License-Identifier: Apache-2.0
import ctypes
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


@app.route("/BenchmarkTest00079", methods=["POST"])
def BenchmarkTest00079():
    origin_value = request.headers.get('Origin', '')
    data = RequestPayload(origin_value).value
    count = int(str(data))
    records = ctypes.create_string_buffer(ctypes.c_uint32(count * 64).value)
    return jsonify({'allocated': len(records)}), 200
