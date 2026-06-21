# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest30227():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
