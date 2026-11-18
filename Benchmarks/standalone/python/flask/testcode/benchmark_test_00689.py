# SPDX-License-Identifier: Apache-2.0
import bleach
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


@app.route("/BenchmarkTest00689", methods=["POST"])
def BenchmarkTest00689():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    processed = bleach.clean(data)
    return '<div>' + str(processed) + '</div>'
