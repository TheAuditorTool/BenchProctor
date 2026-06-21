# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest81477():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200
