# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
from app_runtime import auth_check


def BenchmarkTest79944():
    field_value = request.form.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
