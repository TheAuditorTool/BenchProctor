# SPDX-License-Identifier: Apache-2.0
from lxml import etree
import re
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00193", methods=["POST"])
def BenchmarkTest00193():
    ua_value = request.headers.get('User-Agent', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    if not re.fullmatch("^[a-zA-Z0-9 _.%~\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    find_user = etree.XPath('/users/user[@name="' + str(processed) + '"]')
    find_user(tree)
    return jsonify({"result": "success"})
