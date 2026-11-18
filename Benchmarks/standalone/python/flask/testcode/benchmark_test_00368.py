# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00368", methods=["POST"])
def BenchmarkTest00368():
    env_value = os.environ.get('APP_INPUT', '')
    kind = 'json' if str(env_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            data = str(env_value).strip()
        case _:
            data = str(env_value)
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
