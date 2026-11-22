# SPDX-License-Identifier: Apache-2.0
from flask import Flask, redirect
import requests
from flask import jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00205", methods=["POST"])
def BenchmarkTest00205():
    api_value = requests.get('https://api.partner.example.com/v1/profile').text
    return redirect(str(api_value))
