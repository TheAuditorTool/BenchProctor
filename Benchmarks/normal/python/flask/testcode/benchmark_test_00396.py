# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest00396():
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
