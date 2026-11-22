# SPDX-License-Identifier: Apache-2.0
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


@app.route("/BenchmarkTest00120", methods=["POST"])
def BenchmarkTest00120():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    if not re.fullmatch("^[a-zA-Z0-9 _.#~\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('/var/app/data/' + str(processed), 'r') as fh:
        content = fh.read()
    return content
