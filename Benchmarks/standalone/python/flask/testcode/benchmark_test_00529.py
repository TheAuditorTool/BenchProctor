# SPDX-License-Identifier: Apache-2.0
import bleach
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


@app.route("/BenchmarkTest00529", methods=["POST"])
def BenchmarkTest00529():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % str(forwarded_ip)
    processed = bleach.clean(data)
    return '<div>' + str(processed) + '</div>'
