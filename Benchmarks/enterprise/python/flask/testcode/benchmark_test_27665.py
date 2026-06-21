# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest27665(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    try:
        processed = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return jsonify({'allocated': allocated}), 200
