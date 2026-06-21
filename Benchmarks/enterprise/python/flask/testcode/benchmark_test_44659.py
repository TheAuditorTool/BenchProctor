# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
from app_runtime import auth_check


def BenchmarkTest44659():
    origin_value = request.headers.get('Origin', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    auth_check('user', data)
    return jsonify({"result": "success"})
