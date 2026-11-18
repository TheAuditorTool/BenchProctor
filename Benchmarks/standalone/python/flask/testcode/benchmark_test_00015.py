# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import Flask, request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00015", methods=["POST"])
def BenchmarkTest00015():
    auth_header = request.headers.get('Authorization', '')
    reader = make_reader(auth_header)
    data = reader()
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(data) + '"]')
    return jsonify({"result": "success"})
