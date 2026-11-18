# SPDX-License-Identifier: Apache-2.0
import yaml
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


@app.route("/BenchmarkTest00304", methods=["POST"])
def BenchmarkTest00304():
    field_value = request.form.get('field', '')
    form = FormData(payload=field_value)
    data = form.payload
    parsed = yaml.safe_load(data)
    return jsonify({'parsed': str(parsed)}), 200
