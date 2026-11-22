# SPDX-License-Identifier: Apache-2.0
import urllib.request
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00338", methods=["POST"])
def BenchmarkTest00338():
    field_value = request.form.get('field', '')
    data = f'{field_value!s}'
    outbound = urllib.request.Request(str(data), headers={'User-Agent': 'report-fetcher/1.0'})
    with urllib.request.urlopen(outbound, timeout=10) as upstream:
        upstream.read()
    return jsonify({"result": "success"})
