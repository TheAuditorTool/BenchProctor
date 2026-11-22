# SPDX-License-Identifier: Apache-2.0
import re
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


@app.route("/BenchmarkTest00169", methods=["POST"])
def BenchmarkTest00169():
    multipart_value = request.form.get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    match = re.match(r'^[^@]+@([^@]+)$', str(data))
    domain = match.group(1)
    return jsonify({'domain': domain}), 200
