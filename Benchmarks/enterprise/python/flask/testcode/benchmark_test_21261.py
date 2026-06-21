# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest21261():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
