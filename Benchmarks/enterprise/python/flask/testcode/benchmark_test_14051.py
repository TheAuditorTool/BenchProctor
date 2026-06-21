# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14051():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
