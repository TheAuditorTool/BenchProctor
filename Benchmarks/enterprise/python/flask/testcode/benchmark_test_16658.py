# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify
import json


def BenchmarkTest16658():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    session['data'] = str(data)
    return jsonify({"result": "success"})
