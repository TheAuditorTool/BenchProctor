# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest57311():
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
