# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42213():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200
