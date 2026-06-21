# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from flask import session


def BenchmarkTest53553():
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
