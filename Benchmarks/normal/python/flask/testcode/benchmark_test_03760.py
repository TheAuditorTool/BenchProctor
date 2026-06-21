# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03760():
    raw_body = request.get_data(as_text=True)
    try:
        processed = max(0, min(int(raw_body), 2147483647))
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return jsonify({'allocated': allocated}), 200
