# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00318", methods=["POST"])
def BenchmarkTest00318():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = str(forwarded_ip).replace('\x00', '')
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    etree.XPathEvaluator(tree)('/users/user[@name="' + str(data) + '"]')
    return jsonify({"result": "success"})
