# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import os
from flask import jsonify


def BenchmarkTest26394():
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
