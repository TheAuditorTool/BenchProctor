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


@app.route("/BenchmarkTest00061", methods=["POST"])
def BenchmarkTest00061():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = (lambda v: v.strip())(forwarded_ip)
    if not re.fullmatch("^[a-zA-Z0-9 _.%~\\-]+$", data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
