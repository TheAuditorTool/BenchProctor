# SPDX-License-Identifier: Apache-2.0
from flask import session
import os
from flask import jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest30376():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})
