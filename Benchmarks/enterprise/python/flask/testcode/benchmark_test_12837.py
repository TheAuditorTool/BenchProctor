# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest12837():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})
