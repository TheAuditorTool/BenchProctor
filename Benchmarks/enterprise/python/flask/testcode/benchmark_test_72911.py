# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72911():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
