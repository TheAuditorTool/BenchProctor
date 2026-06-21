# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import defusedxml.ElementTree


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest12477():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
