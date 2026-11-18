# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request
from flask import jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00085", methods=["POST"])
def BenchmarkTest00085():
    cookie_value = request.cookies.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    return '<div>' + str(data) + '</div>'
