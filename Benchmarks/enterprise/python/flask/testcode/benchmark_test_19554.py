# SPDX-License-Identifier: Apache-2.0
import threading
import os
from flask import jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest19554():
    env_value = os.environ.get('USER_INPUT', '')
    data = normalise_input(env_value)
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})
