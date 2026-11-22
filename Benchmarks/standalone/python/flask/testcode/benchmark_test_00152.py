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


@app.route("/BenchmarkTest00152", methods=["POST"])
def BenchmarkTest00152():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % (origin_value,)
    try:
        _coerced = float(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid number'}), 400
    processed = _coerced
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    etree.XPathEvaluator(tree)('/users/user[@name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
