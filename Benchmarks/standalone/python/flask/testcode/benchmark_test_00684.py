# SPDX-License-Identifier: Apache-2.0
from flask import Flask, request
from flask import jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00684", methods=["POST"])
def BenchmarkTest00684():
    xml_value = request.get_data(as_text=True)
    data = f'{xml_value!s}'
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content
