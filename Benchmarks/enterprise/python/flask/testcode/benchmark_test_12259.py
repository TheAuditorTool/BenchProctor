# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12259():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
