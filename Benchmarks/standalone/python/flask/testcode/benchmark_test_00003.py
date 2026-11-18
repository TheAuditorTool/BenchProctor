# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import Flask, request, jsonify
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00003", methods=["POST"])
def BenchmarkTest00003():
    upload_name = request.files['upload'].filename
    kind = 'json' if str(upload_name).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(upload_name).strip()
        case _:
            data = str(upload_name)
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return jsonify({'token': str(token)}), 200
