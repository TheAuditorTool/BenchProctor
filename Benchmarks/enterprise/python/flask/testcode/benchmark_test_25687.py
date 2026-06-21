# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json
from app_runtime import auth_check


def BenchmarkTest25687(path_param):
    path_value = path_param
    try:
        data = json.loads(path_value).get('value', path_value)
    except (json.JSONDecodeError, AttributeError):
        data = path_value
    auth_check('user', data)
    return jsonify({"result": "success"})
