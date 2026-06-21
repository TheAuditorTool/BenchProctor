# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72294():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
