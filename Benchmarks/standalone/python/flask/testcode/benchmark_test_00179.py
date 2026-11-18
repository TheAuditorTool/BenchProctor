# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
import defusedxml.ElementTree


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


@app.route("/BenchmarkTest00179", methods=["POST"])
def BenchmarkTest00179():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = RequestPayload(json_value).value
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
