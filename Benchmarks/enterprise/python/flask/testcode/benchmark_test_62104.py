# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json
from app_runtime import auth_check


def BenchmarkTest62104():
    secret_value = 'config_secret_test_abc123'
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    auth_check('user', data)
    return jsonify({"result": "success"})
