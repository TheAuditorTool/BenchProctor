# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import json
from app_runtime import auth_check


def BenchmarkTest59081():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return jsonify({"result": "success"})
