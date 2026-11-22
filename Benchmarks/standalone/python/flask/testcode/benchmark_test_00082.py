# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00082", methods=["POST"])
def BenchmarkTest00082():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    plan_labels = {'basic': 'Basic plan', 'pro': 'Pro plan', 'team': 'Team plan'}
    label = plan_labels.get(str(data))
    if label is None:
        return jsonify({'error': 'unknown plan'}), 404
    value = label.upper()
    return jsonify({'plan': value}), 200
