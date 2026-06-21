# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
import json
from app_runtime import auth_check


def BenchmarkTest06856():
    field_value = request.form.get('field', '')
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
