# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify
import json


def BenchmarkTest20996():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    _resp = requests.get(str(data))
    exec(_resp.text)
    return jsonify({"result": "success"})
