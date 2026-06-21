# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import json
from app_runtime import auth_check


def BenchmarkTest02270():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})
