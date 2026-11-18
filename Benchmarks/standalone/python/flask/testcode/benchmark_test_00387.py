# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
import re


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00387", methods=["POST"])
def BenchmarkTest00387():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    pending = list(str(graphql_var).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    exec(str(processed))
    return jsonify({"result": "success"})
