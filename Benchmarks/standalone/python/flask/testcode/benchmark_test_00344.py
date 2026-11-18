# SPDX-License-Identifier: Apache-2.0
import hashlib
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


@app.route("/BenchmarkTest00344", methods=["POST"])
def BenchmarkTest00344():
    multipart_value = request.form.get('multipart_field', '')
    form = FormData(payload=multipart_value)
    data = form.payload
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
