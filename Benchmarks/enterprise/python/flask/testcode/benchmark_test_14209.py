# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest14209():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
