# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Flask, request, jsonify
from pydantic import Field, ValidationError, create_model


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00077", methods=["POST"])
def BenchmarkTest00077():
    referer_value = request.headers.get('Referer', '')
    parts = str(referer_value).split(',')
    data = ' '.join(parts)
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.%\\-]+$")))(value=str(data))
    except ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
