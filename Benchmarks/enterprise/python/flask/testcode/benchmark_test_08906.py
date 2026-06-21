# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest08906():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})
