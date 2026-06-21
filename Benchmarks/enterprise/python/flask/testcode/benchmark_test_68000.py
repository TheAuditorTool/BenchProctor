# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest68000():
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
