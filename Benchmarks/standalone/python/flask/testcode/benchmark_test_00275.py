# SPDX-License-Identifier: Apache-2.0
import subprocess
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


@app.route("/BenchmarkTest00275", methods=["POST"])
def BenchmarkTest00275():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
