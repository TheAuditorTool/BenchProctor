# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest54830():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
