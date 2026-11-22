# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify


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
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    code = compile(str(data), '<rule>', 'exec')
    exec(code)
    return jsonify({"result": "success"})
