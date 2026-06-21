# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04743():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
