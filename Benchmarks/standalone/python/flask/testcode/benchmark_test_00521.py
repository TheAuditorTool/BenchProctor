# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import Flask, jsonify
import re


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00521/<path_param>", methods=["POST"])
def BenchmarkTest00521(path_param):
    path_value = path_param
    if not re.fullmatch("^(asc|desc|name|created)$", str(path_value)):
        return jsonify({'error': 'forbidden'}), 400
    processed = path_value
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
