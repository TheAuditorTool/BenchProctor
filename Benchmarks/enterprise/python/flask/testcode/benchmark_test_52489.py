# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52489():
    field_value = request.form.get('field', '')
    data = '%s' % str(field_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
