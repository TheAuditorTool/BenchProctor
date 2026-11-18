# SPDX-License-Identifier: Apache-2.0
import subprocess
import re
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00370", methods=["POST"])
def BenchmarkTest00370():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
