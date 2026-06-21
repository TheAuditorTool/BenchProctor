# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest46382():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    os.remove(str(data))
    return jsonify({"result": "success"})
