# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import time


def relay_value(value):
    return value

def BenchmarkTest52036():
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    if time.time() > 1000000000:
        eval(str(data))
    return jsonify({"result": "success"})
