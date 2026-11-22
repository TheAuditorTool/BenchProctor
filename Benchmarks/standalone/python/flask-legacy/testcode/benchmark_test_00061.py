# SPDX-License-Identifier: Apache-2.0
import os
import re
from flask import Flask, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00061", methods=["POST"])
def BenchmarkTest00061():
    env_value = os.environ.get('APP_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.unlink('/var/app/data/' + str(processed))
    return jsonify({"result": "success"})
