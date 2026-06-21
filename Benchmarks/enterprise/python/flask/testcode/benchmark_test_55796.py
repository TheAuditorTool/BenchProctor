# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55796():
    field_value = request.form.get('field', '')
    kind = 'json' if str(field_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = field_value
            data = parsed
        case _:
            data = field_value
    return jsonify({'error': 'An internal error occurred'}), 500
