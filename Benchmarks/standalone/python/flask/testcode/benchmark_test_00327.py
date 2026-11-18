# SPDX-License-Identifier: Apache-2.0
import yaml
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


@app.route("/BenchmarkTest00327", methods=["POST"])
def BenchmarkTest00327():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    pending = list(str(comment_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
