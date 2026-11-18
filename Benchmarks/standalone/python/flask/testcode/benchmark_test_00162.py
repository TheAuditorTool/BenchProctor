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


@app.route("/BenchmarkTest00162", methods=["POST"])
def BenchmarkTest00162():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    with open('/var/app/data/' + str(forwarded_ip), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
