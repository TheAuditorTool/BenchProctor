# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49907():
    multipart_value = request.form.get('multipart_field', '')
    data = '%s' % str(multipart_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200
