# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest72751():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
