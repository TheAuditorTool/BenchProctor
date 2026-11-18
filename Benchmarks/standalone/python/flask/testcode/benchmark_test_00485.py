# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import Flask, request, jsonify
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00485", methods=["POST"])
def BenchmarkTest00485():
    raw_body = request.get_data(as_text=True)
    data = RequestPayload(raw_body).value
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return jsonify({'token': str(token)}), 200
