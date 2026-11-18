# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import Flask, jsonify
import re
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00547", methods=["POST"])
def BenchmarkTest00547():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = (lambda v: v.strip())(db_value)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
