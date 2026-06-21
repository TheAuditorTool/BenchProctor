# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest68903():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
