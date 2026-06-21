# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest21820():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
