# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest19744():
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    return jsonify({'error': 'An internal error occurred'}), 500
