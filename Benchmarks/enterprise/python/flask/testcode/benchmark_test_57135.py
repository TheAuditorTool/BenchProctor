# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest57135():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
