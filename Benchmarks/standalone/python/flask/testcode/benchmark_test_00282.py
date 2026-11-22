# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import Flask, request, jsonify
import base64
import pickle


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


@app.route("/BenchmarkTest00282", methods=["POST"])
def BenchmarkTest00282():
    raw_body = request.get_data(as_text=True)
    form = FormData(payload=raw_body)
    data = form.payload
    pickle.loads(base64.b64decode(data))
    return jsonify({"result": "success"})
