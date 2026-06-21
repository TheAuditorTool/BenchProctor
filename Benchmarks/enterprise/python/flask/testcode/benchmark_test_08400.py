# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest08400():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    divisor = int(str(data)) if str(data).isdigit() else 1
    if divisor == 0:
        return jsonify({'error': 'zero division'}), 400
    result = 100 / divisor
    return jsonify({"result": "success"})
