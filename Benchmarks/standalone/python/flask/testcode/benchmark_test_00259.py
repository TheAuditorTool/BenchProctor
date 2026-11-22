# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
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


@app.route("/BenchmarkTest00259", methods=["POST"])
def BenchmarkTest00259():
    user_id = request.args.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    s = socket.create_connection((urllib.parse.urlparse(str(data)).hostname, 80))
    s.close()
    return jsonify({"result": "success"})
