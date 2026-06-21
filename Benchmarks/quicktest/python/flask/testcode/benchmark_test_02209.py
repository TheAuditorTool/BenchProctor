# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest02209():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
