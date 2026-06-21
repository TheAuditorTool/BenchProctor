# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
import json
from app_runtime import auth_check


def BenchmarkTest57826(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
