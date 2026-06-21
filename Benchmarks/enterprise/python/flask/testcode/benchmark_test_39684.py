# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest39684():
    env_value = os.environ.get('USER_INPUT', '')
    data = normalise_input(env_value)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
