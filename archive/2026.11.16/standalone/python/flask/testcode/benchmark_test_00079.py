# SPDX-License-Identifier: Apache-2.0
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


@app.route("/BenchmarkTest00079", methods=["POST"])
def BenchmarkTest00079():
    field_value = request.form.get('field', '')
    reader = make_reader(field_value)
    data = reader()
    eval(str(data))
    return jsonify({"result": "success"})
