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


@app.route("/BenchmarkTest00088", methods=["POST"])
def BenchmarkTest00088():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ' '.join(parts)
    current_app.config['ACTIVE_TENANT'] = str(data)
    return jsonify({"result": "success"})
