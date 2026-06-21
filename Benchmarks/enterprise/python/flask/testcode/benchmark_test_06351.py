# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest06351():
    env_value = os.environ.get('USER_INPUT', '')
    if str(env_value) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
