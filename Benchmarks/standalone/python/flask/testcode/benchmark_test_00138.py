# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
import re


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


@app.route("/BenchmarkTest00138/<path_param>", methods=["POST"])
def BenchmarkTest00138(path_param):
    path_value = path_param
    reader = make_reader(path_value)
    data = reader()
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return '<div>' + str(processed) + '</div>'
