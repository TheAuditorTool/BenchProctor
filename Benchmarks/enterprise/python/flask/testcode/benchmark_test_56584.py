# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56584():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
