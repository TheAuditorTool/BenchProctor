# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01789():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(processed)}
