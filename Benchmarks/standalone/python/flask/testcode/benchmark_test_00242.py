# SPDX-License-Identifier: Apache-2.0
from flask import Flask, Response
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


@app.route("/BenchmarkTest00242", methods=["POST"])
def BenchmarkTest00242():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    parts = []
    for token in str(db_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    resp = Response(mimetype='text/html')
    resp.stream.write('<div>' + str(data) + '</div>')
    return resp
