# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest00742():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    return jsonify({'error': 'An internal error occurred'}), 500
