# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import Flask, request
from flask import jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00237", methods=["POST"])
def BenchmarkTest00237():
    origin_value = request.headers.get('Origin', '')
    form = FormData(payload=origin_value)
    data = form.payload
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
