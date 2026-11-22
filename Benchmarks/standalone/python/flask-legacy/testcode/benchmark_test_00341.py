# SPDX-License-Identifier: Apache-2.0
import random
from dataclasses import dataclass
from flask import Flask, request, jsonify
from app_runtime import db


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


@app.route("/BenchmarkTest00341", methods=["POST"])
def BenchmarkTest00341():
    cookie_value = request.cookies.get('session_token', '')
    form = FormData(payload=cookie_value)
    data = form.payload
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return jsonify({'token': str(token)}), 200
