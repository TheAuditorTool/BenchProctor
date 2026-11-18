# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request
from flask import jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00128", methods=["POST"])
def BenchmarkTest00128():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    return '<div>' + str(data) + '</div>'
