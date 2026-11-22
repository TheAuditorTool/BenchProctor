# SPDX-License-Identifier: Apache-2.0
import numpy as np
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00136", methods=["POST"])
def BenchmarkTest00136():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % (json_value,)
    quantity = int(str(data))
    total_cents = np.int32(quantity) * np.int32(1999)
    return jsonify({'total_cents': int(total_cents)}), 200
