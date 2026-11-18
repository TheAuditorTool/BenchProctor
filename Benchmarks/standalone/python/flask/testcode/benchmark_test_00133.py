# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, jsonify
import ctypes


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


@app.route("/BenchmarkTest00133", methods=["POST"])
def BenchmarkTest00133():
    env_value = os.environ.get('APP_INPUT', '')
    data = RequestPayload(env_value).value
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
