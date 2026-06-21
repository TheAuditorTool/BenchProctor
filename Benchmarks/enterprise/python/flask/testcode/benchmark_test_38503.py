# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest38503():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
