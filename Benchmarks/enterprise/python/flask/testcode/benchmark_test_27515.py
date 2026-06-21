# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest27515():
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
