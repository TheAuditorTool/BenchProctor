# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest51905():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})
