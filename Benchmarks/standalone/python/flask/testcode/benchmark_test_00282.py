# SPDX-License-Identifier: Apache-2.0
import subprocess
import jsonschema
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


@app.route("/BenchmarkTest00282", methods=["POST"])
def BenchmarkTest00282():
    env_value = os.environ.get('APP_INPUT', '')
    data = ' '.join(str(env_value).split())
    try:
        jsonschema.validate(str(data), {'type': 'string', 'pattern': "^[a-zA-Z0-9 _.%\\-]+$"})
    except jsonschema.ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
