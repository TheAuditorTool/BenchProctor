# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import os
from flask import jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest19503():
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
