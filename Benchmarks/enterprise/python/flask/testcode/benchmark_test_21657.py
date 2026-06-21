# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21657():
    field_value = request.form.get('field', '')
    data = f'{field_value}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
