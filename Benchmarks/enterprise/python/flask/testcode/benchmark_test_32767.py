# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest32767():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})
