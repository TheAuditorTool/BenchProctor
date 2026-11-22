# SPDX-License-Identifier: Apache-2.0
from flask import Flask, abort
from flask import redirect
from dataclasses import dataclass
from app_runtime import db
from flask import jsonify


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00004", methods=["POST"])
def BenchmarkTest00004():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    form = FormData(payload=comment_value)
    data = form.payload
    abort(redirect(str(data)))
