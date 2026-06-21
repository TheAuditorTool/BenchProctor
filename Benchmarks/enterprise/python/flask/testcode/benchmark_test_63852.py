# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest63852():
    env_value = os.environ.get('USER_INPUT', '')
    return jsonify({'error': 'An internal error occurred'}), 500
