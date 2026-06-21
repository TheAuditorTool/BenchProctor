# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest16160():
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    return jsonify({'error': 'An internal error occurred'}), 500
