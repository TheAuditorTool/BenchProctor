# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest06722():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
