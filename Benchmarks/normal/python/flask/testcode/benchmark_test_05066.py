# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json
from app_runtime import auth_check


def BenchmarkTest05066():
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    auth_check('user', data)
    return jsonify({"result": "success"})
