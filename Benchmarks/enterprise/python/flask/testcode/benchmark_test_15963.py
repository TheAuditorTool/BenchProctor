# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15963():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    try:
        processed = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return jsonify({'allocated': allocated}), 200
