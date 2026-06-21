# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
from app_runtime import auth_check


def BenchmarkTest28441():
    xml_value = request.get_data(as_text=True)
    try:
        data = json.loads(xml_value).get('value', xml_value)
    except (json.JSONDecodeError, AttributeError):
        data = xml_value
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
