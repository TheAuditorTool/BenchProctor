# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import os
from flask import Flask, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00032", methods=["POST"])
def BenchmarkTest00032():
    env_value = os.environ.get('APP_INPUT', '')
    data = ' '.join(str(env_value).split())
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(data) + '"]')
    return jsonify({"result": "success"})
