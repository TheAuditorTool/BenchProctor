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


@app.route("/BenchmarkTest00334/<path_param>", methods=["POST"])
def BenchmarkTest00334(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid number'}), 400
    processed = _coerced
    eval(str(processed))
    return jsonify({"result": "success"})
