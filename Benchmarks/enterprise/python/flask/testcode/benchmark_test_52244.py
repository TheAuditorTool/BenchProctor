# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52244():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
