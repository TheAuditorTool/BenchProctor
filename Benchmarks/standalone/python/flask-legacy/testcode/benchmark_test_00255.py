# SPDX-License-Identifier: Apache-2.0
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


@app.route("/BenchmarkTest00255", methods=["POST"])
def BenchmarkTest00255():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    code = compile(str(processed), '<rule>', 'exec')
    exec(code)
    return jsonify({"result": "success"})
