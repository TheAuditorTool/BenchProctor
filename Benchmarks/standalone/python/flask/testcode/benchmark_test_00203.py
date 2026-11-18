# SPDX-License-Identifier: Apache-2.0
from flask import Flask, redirect
from flask import request
from flask import jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00203", methods=["POST"])
def BenchmarkTest00203():
    raw_body = request.get_data(as_text=True)
    if raw_body:
        data = raw_body
    else:
        data = ''
    return redirect(str(data))
