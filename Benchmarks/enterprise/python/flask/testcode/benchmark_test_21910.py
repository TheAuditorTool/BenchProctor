# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest21910():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
