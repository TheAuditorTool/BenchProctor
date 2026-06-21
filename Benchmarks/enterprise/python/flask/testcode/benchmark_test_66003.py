# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66003():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    try:
        processed = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return jsonify({'allocated': allocated}), 200
