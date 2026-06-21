# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03227():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
