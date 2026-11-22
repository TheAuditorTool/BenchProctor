# SPDX-License-Identifier: Apache-2.0
import os
from flask import Flask, jsonify
from pathlib import Path


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00073", methods=["POST"])
def BenchmarkTest00073():
    env_value = os.environ.get('APP_INPUT', '')
    data = '%s' % (env_value,)
    Path('/var/app/data/' + str(data)).write_text('data')
    return jsonify({"result": "success"})
