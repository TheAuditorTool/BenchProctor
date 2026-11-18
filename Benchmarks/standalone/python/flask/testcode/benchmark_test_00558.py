# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00558", methods=["POST"])
def BenchmarkTest00558():
    host_value = request.headers.get('Host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
