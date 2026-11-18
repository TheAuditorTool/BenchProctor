# SPDX-License-Identifier: Apache-2.0
from flask import Flask, redirect
from dataclasses import dataclass
from flask import request
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


@app.route("/BenchmarkTest00006", methods=["POST"])
def BenchmarkTest00006():
    auth_header = request.headers.get('Authorization', '')
    form = FormData(payload=auth_header)
    data = form.payload
    return redirect(str(data))
