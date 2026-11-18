# SPDX-License-Identifier: Apache-2.0
import bleach
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


@app.route("/BenchmarkTest00034", methods=["POST"])
def BenchmarkTest00034():
    header_value = request.headers.get('X-Custom-Header', '')
    reader = make_reader(header_value)
    data = reader()
    processed = bleach.clean(data)
    return '<div>' + str(processed) + '</div>'
