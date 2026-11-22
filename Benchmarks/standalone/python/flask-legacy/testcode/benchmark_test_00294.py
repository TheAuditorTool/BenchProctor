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


@app.route("/BenchmarkTest00294", methods=["POST"])
def BenchmarkTest00294():
    user_id = request.args.get('id', '')
    data = f'{user_id!s}'
    abort(redirect(str(data)))
