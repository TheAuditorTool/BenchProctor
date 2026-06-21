# SPDX-License-Identifier: Apache-2.0
import secrets
import os
from flask import jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest00139():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
