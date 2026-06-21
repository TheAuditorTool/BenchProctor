# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import os
from flask import jsonify


def BenchmarkTest28778():
    env_value = os.environ.get('USER_INPUT', '')
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(env_value), secure=True, httponly=True, samesite='Strict')
    return resp
