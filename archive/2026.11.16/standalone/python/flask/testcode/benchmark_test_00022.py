# SPDX-License-Identifier: Apache-2.0
import os
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


@app.route("/BenchmarkTest00022", methods=["POST"])
def BenchmarkTest00022():
    upload_name = request.files['doc'].filename
    form = FormData(payload=upload_name)
    data = form.payload
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
