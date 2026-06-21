# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest17913():
    env_value = os.environ.get('USER_INPUT', '')
    if str(env_value) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
