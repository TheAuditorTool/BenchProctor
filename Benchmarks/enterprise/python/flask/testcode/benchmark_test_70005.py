# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest70005():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
