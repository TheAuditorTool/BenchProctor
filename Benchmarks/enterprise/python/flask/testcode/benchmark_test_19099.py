# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import json


def BenchmarkTest19099():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    os.remove(str(data))
    return jsonify({"result": "success"})
