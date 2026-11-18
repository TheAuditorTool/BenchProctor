# SPDX-License-Identifier: Apache-2.0
import os
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


@app.route("/BenchmarkTest00116", methods=["POST"])
def BenchmarkTest00116():
    upload_name = request.files['doc'].filename
    data = RequestPayload(upload_name).value
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
