# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import Flask, request, jsonify


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


@app.route("/BenchmarkTest00095", methods=["POST"])
def BenchmarkTest00095():
    origin_value = request.headers.get('Origin', '')
    reader = make_reader(origin_value)
    data = reader()
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
