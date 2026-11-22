# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
from pathlib import Path


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00287", methods=["POST"])
def BenchmarkTest00287():
    referer_value = request.headers.get('Referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    Path('/var/app/data/' + str(data)).write_text('data')
    return jsonify({"result": "success"})
