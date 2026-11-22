# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
import subprocess


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00034", methods=["POST"])
def BenchmarkTest00034():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
