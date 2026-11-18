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


@app.route("/BenchmarkTest00156", methods=["POST"])
def BenchmarkTest00156():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    form = FormData(payload=json_value)
    data = form.payload
    token = '%032x' % random.getrandbits(128)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return jsonify({'token': str(token)}), 200
