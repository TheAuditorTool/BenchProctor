# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, make_response
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


@app.route("/BenchmarkTest00222", methods=["POST"])
def BenchmarkTest00222():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    parts = str(comment_value).split(',')
    data = ' '.join(parts)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
