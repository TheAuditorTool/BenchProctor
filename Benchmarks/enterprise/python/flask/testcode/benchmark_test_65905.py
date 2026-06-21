# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest65905():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
