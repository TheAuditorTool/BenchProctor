# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, session
from flask import jsonify
from app_runtime import db


app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY") or os.urandom(32).hex()


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00608", methods=["POST"])
def BenchmarkTest00608():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = comment_value if comment_value else 'default'
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid number'}), 400
    processed = _coerced
    session['data'] = str(processed)
    return jsonify({"result": "success"})
