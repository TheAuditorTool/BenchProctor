# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import json
from app_runtime import auth_check


def BenchmarkTest78819():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
