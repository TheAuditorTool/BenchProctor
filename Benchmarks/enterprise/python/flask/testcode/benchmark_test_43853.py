# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import os
from flask import jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest43853():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
