# SPDX-License-Identifier: Apache-2.0
import html
from app_runtime import db
from flask import Flask, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00513", methods=["POST"])
def BenchmarkTest00513():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data, _sep, _rest = str(db_value).partition('\x00')
    processed = html.escape(data)
    return '<div>' + str(processed) + '</div>'
