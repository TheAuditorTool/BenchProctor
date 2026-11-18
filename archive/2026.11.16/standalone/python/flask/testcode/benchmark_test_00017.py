# SPDX-License-Identifier: Apache-2.0
from flask import Flask, redirect
import requests
from flask import jsonify


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


@app.route("/BenchmarkTest00017", methods=["POST"])
def BenchmarkTest00017():
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    data = RequestPayload(api_value).value
    return redirect(str(data))
