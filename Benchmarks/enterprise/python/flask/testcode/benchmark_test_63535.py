# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest63535():
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    return jsonify({'error': 'An internal error occurred'}), 500
