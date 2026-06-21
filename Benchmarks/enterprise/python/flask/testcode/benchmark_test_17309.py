# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json
from app_runtime import auth_check


def BenchmarkTest17309():
    referer_value = request.headers.get('Referer', '')
    try:
        data = json.loads(referer_value).get('value', referer_value)
    except (json.JSONDecodeError, AttributeError):
        data = referer_value
    auth_check('user', data)
    return jsonify({"result": "success"})
