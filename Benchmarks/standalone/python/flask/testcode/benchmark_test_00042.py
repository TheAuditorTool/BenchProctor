# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
import socket
import urllib.parse


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00042/<path_param>", methods=["POST"])
def BenchmarkTest00042(path_param):
    path_value = path_param
    pending = list(str(path_value).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    s = socket.create_connection((urllib.parse.urlparse(str(data)).hostname, 80))
    s.close()
    return jsonify({"result": "success"})
