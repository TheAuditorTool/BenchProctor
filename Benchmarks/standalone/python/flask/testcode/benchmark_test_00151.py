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


@app.route("/BenchmarkTest00151", methods=["POST"])
def BenchmarkTest00151():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    parts = str(forwarded_ip).split(',')
    data = ' '.join(parts)
    processed = html.escape(data)
    return '<div>' + str(processed) + '</div>'
