# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest28905():
    env_value = os.environ.get('USER_INPUT', '')
    if str(env_value) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
