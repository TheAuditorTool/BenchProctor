# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75158():
    upload_name = request.files['upload'].filename
    try:
        processed = max(0, min(int(upload_name), 2147483647))
    except (TypeError, ValueError):
        return jsonify({'error': 'invalid integer'}), 400
    requested = int(processed)
    allocated = min(requested + 1, 2147483647)
    return jsonify({'allocated': allocated}), 200
