# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import Flask, request, jsonify
from marshmallow import Schema, fields, validate, ValidationError


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00631", methods=["POST"])
def BenchmarkTest00631():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json_value if json_value else 'default'
    try:
        Schema.from_dict({'value': fields.Str(validate=validate.Regexp("^[a-zA-Z0-9 _.%\\-]+$"))})().load({'value': str(data)})
    except ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return jsonify({"result": "success"})
