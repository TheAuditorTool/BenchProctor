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


@app.route("/BenchmarkTest00037", methods=["POST"])
def BenchmarkTest00037():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
