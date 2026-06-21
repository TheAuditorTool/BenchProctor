# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57100():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
