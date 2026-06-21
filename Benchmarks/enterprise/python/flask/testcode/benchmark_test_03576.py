# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest03576():
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    return jsonify({'error': 'An internal error occurred'}), 500
