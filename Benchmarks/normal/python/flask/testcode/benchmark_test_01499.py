# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
import json
from app_runtime import auth_check


def BenchmarkTest01499():
    ua_value = request.headers.get('User-Agent', '')
    try:
        data = json.loads(ua_value).get('value', ua_value)
    except (json.JSONDecodeError, AttributeError):
        data = ua_value
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
