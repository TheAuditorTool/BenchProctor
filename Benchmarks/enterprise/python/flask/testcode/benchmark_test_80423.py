# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80423():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
