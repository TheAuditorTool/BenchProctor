# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22938():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
