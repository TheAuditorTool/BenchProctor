# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22663():
    user_id = request.args.get('id', '')
    try:
        processed = max(0, min(int(user_id), 2147483647))
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return jsonify({'allocated': allocated}), 200
