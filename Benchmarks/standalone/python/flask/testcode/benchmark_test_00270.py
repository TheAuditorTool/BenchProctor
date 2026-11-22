# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
import re
from pathlib import Path


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00270/<path_param>", methods=["POST"])
def BenchmarkTest00270(path_param):
    path_value = path_param
    kind = 'json' if str(path_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(path_value).strip()
        case _:
            data = str(path_value)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    Path('/var/app/data/' + str(processed)).write_text('data')
    return jsonify({"result": "success"})
