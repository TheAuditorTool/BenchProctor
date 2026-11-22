# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
import json


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00056/<path_param>", methods=["POST"])
def BenchmarkTest00056(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    code = compile(str(processed), '<rule>', 'exec')
    exec(code)
    return jsonify({"result": "success"})
