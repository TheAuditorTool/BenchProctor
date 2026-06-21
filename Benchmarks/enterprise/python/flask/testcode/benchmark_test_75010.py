# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def relay_value(value):
    return value

def BenchmarkTest75010():
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    return jsonify({'error': 'An internal error occurred'}), 500
