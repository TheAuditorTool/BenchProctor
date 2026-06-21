# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01964():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
