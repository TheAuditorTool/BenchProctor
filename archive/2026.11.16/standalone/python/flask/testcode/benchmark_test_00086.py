# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import Flask, jsonify
import defusedxml.ElementTree
from app_runtime import db


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


@app.route("/BenchmarkTest00086", methods=["POST"])
def BenchmarkTest00086():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    form = FormData(payload=comment_value)
    data = form.payload
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
