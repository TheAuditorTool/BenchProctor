# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest17471():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = env_value
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
