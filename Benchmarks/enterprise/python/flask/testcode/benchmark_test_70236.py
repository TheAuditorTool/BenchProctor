# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify
import json


def BenchmarkTest70236():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})
