# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import os
from flask import jsonify
import json


def BenchmarkTest06877():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
