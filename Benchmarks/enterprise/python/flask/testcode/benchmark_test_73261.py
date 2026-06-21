# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest73261():
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
