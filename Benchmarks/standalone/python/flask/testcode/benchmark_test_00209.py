# SPDX-License-Identifier: Apache-2.0
from flask import Flask, abort
from flask import redirect
from flask import request
from flask import jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00209", methods=["POST"])
def BenchmarkTest00209():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    abort(redirect(str(data)))
