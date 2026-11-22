# SPDX-License-Identifier: Apache-2.0
import numpy as np
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


@app.route("/BenchmarkTest00062", methods=["POST"])
def BenchmarkTest00062():
    env_value = os.environ.get('APP_INPUT', '')
    data = env_value if env_value else 'default'
    quantity = int(str(data))
    total_cents = np.int32(quantity) * np.int32(1999)
    return jsonify({'total_cents': int(total_cents)}), 200
