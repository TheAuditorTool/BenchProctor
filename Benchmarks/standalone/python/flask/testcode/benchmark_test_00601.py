# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00601", methods=["POST"])
def BenchmarkTest00601():
    multipart_value = request.form.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ' '.join(parts)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
