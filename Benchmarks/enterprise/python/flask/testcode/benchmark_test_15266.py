# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest15266():
    env_value = os.environ.get('USER_INPUT', '')
    try:
        result = int(str(env_value))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
