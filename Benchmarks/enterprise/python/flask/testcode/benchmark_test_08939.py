# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest08939():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
