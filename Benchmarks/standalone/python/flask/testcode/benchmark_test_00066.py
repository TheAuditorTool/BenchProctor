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


@app.route("/BenchmarkTest00066", methods=["POST"])
def BenchmarkTest00066():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '{}'.format(graphql_var)
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(data) + '"]')
    return jsonify({"result": "success"})
