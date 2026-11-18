# SPDX-License-Identifier: Apache-2.0
from flask import Flask, redirect
from app_runtime import db
from flask import jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00472", methods=["POST"])
def BenchmarkTest00472():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = bytes.fromhex(db_value).decode('utf-8', 'ignore')
    return redirect(str(data))
