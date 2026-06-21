# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest13726(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    try:
        processed = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return jsonify({'allocated': allocated}), 200
