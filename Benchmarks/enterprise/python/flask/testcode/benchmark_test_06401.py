# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest06401():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
