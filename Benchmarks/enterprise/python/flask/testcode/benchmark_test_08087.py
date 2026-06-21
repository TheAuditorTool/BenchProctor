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

def BenchmarkTest08087():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200
