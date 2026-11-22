# SPDX-License-Identifier: Apache-2.0
import json
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00289", methods=["POST"])
def BenchmarkTest00289():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    eval(str(processed))
    return jsonify({"result": "success"})
