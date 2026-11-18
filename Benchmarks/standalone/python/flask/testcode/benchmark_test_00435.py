# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify
import base64
import pickle


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00435", methods=["POST"])
def BenchmarkTest00435():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    pickle.loads(base64.b64decode(data))
    return jsonify({"result": "success"})
