# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import os
from flask import jsonify


def BenchmarkTest29290():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
