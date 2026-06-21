# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest30088():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
