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


@app.route("/BenchmarkTest00294", methods=["POST"])
def BenchmarkTest00294():
    raw_body = request.get_data(as_text=True)
    data = '{}'.format(raw_body)
    return '', 302, {'Location': str(data)}
