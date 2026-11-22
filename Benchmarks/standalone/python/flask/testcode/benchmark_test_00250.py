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


@app.route("/BenchmarkTest00250/<path_param>", methods=["POST"])
def BenchmarkTest00250(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
