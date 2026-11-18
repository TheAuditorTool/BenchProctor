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


@app.route("/BenchmarkTest00559", methods=["POST"])
def BenchmarkTest00559():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    processed = html.escape(data)
    return '<div>' + str(processed) + '</div>'
