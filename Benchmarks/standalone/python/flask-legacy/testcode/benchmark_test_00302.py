# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import Flask, jsonify
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00302", methods=["POST"])
def BenchmarkTest00302():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    kind = 'json' if str(comment_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(comment_value).strip()
        case _:
            data = str(comment_value)
    digest = hashlib.sha3_256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
