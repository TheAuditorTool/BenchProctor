# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import Flask, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00017/<path_param>", methods=["POST"])
def BenchmarkTest00017(path_param):
    path_value = path_param
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(path_value) + '"]')
    return jsonify({"result": "success"})
