# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, make_response
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00500", methods=["POST"])
def BenchmarkTest00500():
    upload_name = request.files['upload'].filename
    form = FormData(payload=upload_name)
    data = form.payload
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
