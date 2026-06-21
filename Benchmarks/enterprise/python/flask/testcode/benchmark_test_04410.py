# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04410():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
