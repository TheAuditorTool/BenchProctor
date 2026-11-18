# SPDX-License-Identifier: Apache-2.0
from flask import Flask, jsonify
from lxml import etree
from app_runtime import db


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00499", methods=["POST"])
def BenchmarkTest00499():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(comment_value).encode(), _parser)
    return jsonify({"result": "success"})
