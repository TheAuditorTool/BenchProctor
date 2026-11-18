# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import Flask, request, jsonify
import ctypes


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


@app.route("/BenchmarkTest00613", methods=["POST"])
def BenchmarkTest00613():
    raw_body = request.get_data(as_text=True)
    form = FormData(payload=raw_body)
    data = form.payload
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return jsonify({'wrapped': wrapped}), 200
