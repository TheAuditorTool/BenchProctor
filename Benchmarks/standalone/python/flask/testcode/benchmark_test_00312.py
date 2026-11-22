# SPDX-License-Identifier: Apache-2.0
import html
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


@app.route("/BenchmarkTest00312", methods=["POST"])
def BenchmarkTest00312():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    processed = html.escape(data)
    return '<div>' + str(processed) + '</div>'
