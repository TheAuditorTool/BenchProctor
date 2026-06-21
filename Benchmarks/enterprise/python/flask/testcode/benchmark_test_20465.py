# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20465():
    raw_body = request.get_data(as_text=True)
    if raw_body not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = raw_body
    return str(processed), 200, {'Content-Type': 'text/html'}
