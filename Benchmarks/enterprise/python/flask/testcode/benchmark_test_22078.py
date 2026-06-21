# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest22078():
    env_value = os.environ.get('USER_INPUT', '')
    return jsonify({'error': str(env_value), 'stack': repr(locals())}), 500
