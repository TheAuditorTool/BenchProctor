# SPDX-License-Identifier: Apache-2.0
import re
from dataclasses import dataclass
from flask import Flask, request, jsonify


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


@app.route("/BenchmarkTest00358", methods=["POST"])
def BenchmarkTest00358():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    form = FormData(payload=json_value)
    data = form.payload
    match = re.match(r'^[^@]+@([^@]+)$', str(data))
    domain = match.group(1)
    return jsonify({'domain': domain}), 200
