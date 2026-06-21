# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79100():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
