# SPDX-License-Identifier: Apache-2.0
import bleach
import base64
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


@app.route("/BenchmarkTest00217", methods=["POST"])
def BenchmarkTest00217():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = base64.b64decode(db_value).decode('utf-8', 'ignore')
    processed = bleach.clean(data)
    return '<div>' + str(processed) + '</div>'
