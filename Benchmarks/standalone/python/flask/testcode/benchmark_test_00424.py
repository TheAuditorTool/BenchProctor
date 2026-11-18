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


@app.route("/BenchmarkTest00424", methods=["POST"])
def BenchmarkTest00424():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = ' '.join(str(comment_value).split())
    _parser = etree.XMLParser(resolve_entities=True, no_network=False)
    etree.fromstring(str(data).encode(), _parser)
    return jsonify({"result": "success"})
