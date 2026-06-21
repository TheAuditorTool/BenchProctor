# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57159():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
