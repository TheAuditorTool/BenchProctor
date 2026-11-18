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


@app.route("/BenchmarkTest00606", methods=["POST"])
def BenchmarkTest00606():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    return '<div>' + str(data) + '</div>'
