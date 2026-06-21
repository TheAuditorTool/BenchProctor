# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json
from app_runtime import auth_check


def BenchmarkTest67090():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    try:
        data = json.loads(secret_value).get('value', secret_value)
    except (json.JSONDecodeError, AttributeError):
        data = secret_value
    auth_check('user', data)
    return jsonify({"result": "success"})
