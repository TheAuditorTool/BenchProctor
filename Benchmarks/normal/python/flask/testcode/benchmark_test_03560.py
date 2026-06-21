# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03560():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
