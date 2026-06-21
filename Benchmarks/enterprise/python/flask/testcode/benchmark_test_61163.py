# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest61163():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
