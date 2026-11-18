# SPDX-License-Identifier: Apache-2.0
import secrets
from dataclasses import dataclass
from flask import Flask, jsonify
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


@app.route("/BenchmarkTest00362/<path_param>", methods=["POST"])
def BenchmarkTest00362(path_param):
    path_value = path_param
    form = FormData(payload=path_value)
    data = form.payload
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return jsonify({'token': str(token)}), 200
