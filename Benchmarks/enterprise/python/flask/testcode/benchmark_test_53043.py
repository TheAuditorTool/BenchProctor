# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest53043():
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    try:
        processed = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return jsonify({'allocated': allocated}), 200
