# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest09179():
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
