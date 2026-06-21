# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest27577():
    env_value = os.environ.get('USER_INPUT', '')
    divisor = int(str(env_value)) if str(env_value).isdigit() else 1
    if divisor == 0:
        return jsonify({'error': 'zero division'}), 400
    result = 100 / divisor
    return jsonify({"result": "success"})
