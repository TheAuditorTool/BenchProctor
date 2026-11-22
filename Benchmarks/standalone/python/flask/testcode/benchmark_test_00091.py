# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
from pathlib import Path


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


@app.route("/BenchmarkTest00091", methods=["POST"])
def BenchmarkTest00091():
    header_value = request.headers.get('X-Custom-Header', '')
    data = RequestPayload(header_value).value
    Path('/var/app/data/' + str(data)).write_text('data')
    return jsonify({"result": "success"})
