# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import Flask, jsonify
from app_runtime import db


def make_reader(raw):
    def read():
        return raw.strip()
    return read

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00247", methods=["POST"])
def BenchmarkTest00247():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    reader = make_reader(comment_value)
    data = reader()
    token = secrets.token_hex(32)
    db.execute('INSERT INTO reset_tokens (account, token) VALUES (?, ?)', (str(data), token))
    return jsonify({'token': str(token)}), 200
