# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00055", methods=["POST"])
def BenchmarkTest00055():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    os.unlink('/var/app/data/' + str(data))
    return jsonify({"result": "success"})
