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


@app.route("/BenchmarkTest00523", methods=["POST"])
def BenchmarkTest00523():
    referer_value = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    processed = bleach.clean(data)
    return '<div>' + str(processed) + '</div>'
