# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest78718():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})
