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


@app.route("/BenchmarkTest00331", methods=["POST"])
def BenchmarkTest00331():
    origin_value = request.headers.get('Origin', '')
    reader = make_reader(origin_value)
    data = reader()
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(data) + '"]')
    return jsonify({"result": "success"})
