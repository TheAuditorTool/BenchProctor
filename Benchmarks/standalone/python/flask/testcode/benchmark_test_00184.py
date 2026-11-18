# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
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


@app.route("/BenchmarkTest00184", methods=["POST"])
def BenchmarkTest00184():
    raw_body = request.get_data(as_text=True)
    reader = make_reader(raw_body)
    data = reader()
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    exec(str(processed))
    return jsonify({"result": "success"})
