# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest70808():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
