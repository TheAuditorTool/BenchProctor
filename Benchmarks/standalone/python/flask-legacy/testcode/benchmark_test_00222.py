# SPDX-License-Identifier: Apache-2.0
from lxml import etree
from flask import Flask, request, jsonify
import json
from pydantic import Field, ValidationError, create_model


app = Flask(__name__)


@app.after_request
def _apply_security_headers(response):
    response.headers["X-Content-Type-Options"] = "nosniff"
    return response


@app.errorhandler(Exception)
def _handle_unexpected(exc):
    return jsonify({"error": "internal"}), 500


@app.route("/BenchmarkTest00222", methods=["POST"])
def BenchmarkTest00222():
    referer_value = request.headers.get('Referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    try:
        create_model('_InputModel', value=(str, Field(regex="^[a-zA-Z0-9 _.%~\\-]+$")))(value=str(data))
    except ValidationError:
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    tree = etree.fromstring(b'<users><user name="admin"/></users>')
    find_user = etree.XPath('/users/user[@name="' + str(processed) + '"]')
    find_user(tree)
    return jsonify({"result": "success"})
