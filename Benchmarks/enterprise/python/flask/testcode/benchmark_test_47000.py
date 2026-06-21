# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest47000():
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
