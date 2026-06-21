# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest57689():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
