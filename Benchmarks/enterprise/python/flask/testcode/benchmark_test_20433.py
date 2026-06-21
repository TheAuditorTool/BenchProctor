# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest20433():
    env_value = os.environ.get('USER_INPUT', '')
    data = (lambda v: v.strip())(env_value)
    return jsonify({'error': 'An internal error occurred'}), 500
