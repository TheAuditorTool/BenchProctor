# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest23249():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
