# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, session
import re
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


@app.route("/BenchmarkTest00539", methods=["POST"])
def BenchmarkTest00539():
    referer_value = request.headers.get('Referer', '')
    form = FormData(payload=referer_value)
    data = form.payload
    if not re.fullmatch("^[a-zA-Z0-9 _.\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    session['data'] = str(processed)
    return jsonify({"result": "success"})
