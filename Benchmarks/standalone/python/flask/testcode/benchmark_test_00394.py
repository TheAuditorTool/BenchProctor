# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, session
from flask import request, jsonify


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00394", methods=["POST"])
def BenchmarkTest00394():
    raw_body = request.get_data(as_text=True)
    data = RequestPayload(raw_body).value
    session['data'] = str(data)
    return jsonify({"result": "success"})
