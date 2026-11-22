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


@app.route("/BenchmarkTest00027", methods=["POST"])
def BenchmarkTest00027():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    _coerced = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    processed = _coerced
    current_app.config['ACTIVE_TENANT'] = str(processed)
    return jsonify({"result": "success"})
