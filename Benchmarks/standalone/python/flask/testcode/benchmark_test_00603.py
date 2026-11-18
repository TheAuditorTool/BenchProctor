# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import Flask, request, jsonify
from pydantic import Field, ValidationError, create_model


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00603", methods=["POST"])
def BenchmarkTest00603():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    try:
        create_model('_InputModel', value=(str, Field(pattern="^[a-zA-Z0-9 _.%~\\-]+$")))(value=str(data))
    except ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    tree.xpath('/users/user[@name="' + str(processed) + '"]')
    return jsonify({"result": "success"})
