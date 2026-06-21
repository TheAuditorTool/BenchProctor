# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67897():
    multipart_value = request.form.get('multipart_field', '')
    match str(multipart_value):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200
