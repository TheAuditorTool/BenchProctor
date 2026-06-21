# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01283():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return str(processed), 200, {'Content-Type': 'text/html'}
