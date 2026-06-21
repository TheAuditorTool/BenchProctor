# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10112():
    field_value = request.form.get('field', '')
    if field_value not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = field_value
    return str(processed), 200, {'Content-Type': 'text/html'}
