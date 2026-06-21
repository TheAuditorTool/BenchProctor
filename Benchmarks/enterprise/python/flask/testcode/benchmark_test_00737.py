# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import os
from flask import jsonify
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest00737():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    if time.time() > 1000000000:
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})
