# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28810():
    field_value = request.form.get('field', '')
    data = '{}'.format(field_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200
