# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
import re


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


@app.route("/BenchmarkTest00278", methods=["POST"])
def BenchmarkTest00278():
    cookie_value = request.cookies.get('session_token', '')
    data = RequestPayload(cookie_value).value
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    code = compile(str(processed), '<rule>', 'exec')
    exec(code)
    return jsonify({"result": "success"})
