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


@app.route("/BenchmarkTest00227", methods=["POST"])
def BenchmarkTest00227():
    env_value = os.environ.get('APP_INPUT', '')
    data = '{}'.format(env_value)
    plan_labels = {'basic': 'Basic plan', 'pro': 'Pro plan', 'team': 'Team plan'}
    label = plan_labels.get(str(data))
    value = label.upper()
    return jsonify({'plan': value}), 200
