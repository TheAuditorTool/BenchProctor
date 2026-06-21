# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest09599():
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    processed = data[:64]
    return jsonify({'error': str(processed), 'stack': repr(locals())}), 500
