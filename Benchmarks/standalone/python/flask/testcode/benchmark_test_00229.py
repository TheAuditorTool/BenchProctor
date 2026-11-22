# SPDX-License-Identifier: Apache-2.0
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


@app.route("/BenchmarkTest00229", methods=["POST"])
def BenchmarkTest00229():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = (lambda v: v.strip())(comment_value)
    code = compile(str(data), '<rule>', 'exec')
    exec(code)
    return jsonify({"result": "success"})
