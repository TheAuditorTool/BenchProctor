# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest41148():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
