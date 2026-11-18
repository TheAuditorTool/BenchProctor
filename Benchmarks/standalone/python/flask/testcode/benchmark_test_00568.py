# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
import base64
import pickle
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00568", methods=["POST"])
def BenchmarkTest00568():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(db_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    pickle.loads(base64.b64decode(data))
    return jsonify({"result": "success"})
