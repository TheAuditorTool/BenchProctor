# SPDX-License-Identifier: Apache-2.0
from flask import Flask, current_app
from flask import request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00224", methods=["POST"])
def BenchmarkTest00224():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = str(graphql_var).replace('\x00', '')
    current_app.config['ACTIVE_TENANT'] = str(data)
    return jsonify({"result": "success"})
