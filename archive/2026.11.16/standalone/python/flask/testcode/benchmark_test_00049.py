# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
import defusedxml.ElementTree


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


@app.route("/BenchmarkTest00049", methods=["POST"])
def BenchmarkTest00049():
    multipart_value = request.form.get('multipart_field', '')
    reader = make_reader(multipart_value)
    data = reader()
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
