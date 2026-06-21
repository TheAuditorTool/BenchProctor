# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest55424():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = to_text(forwarded_ip)
    try:
        processed = max(0, min(int(data), 2147483647))
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return jsonify({'allocated': allocated}), 200
