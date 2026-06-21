# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10330():
    field_value = request.form.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
