# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80856():
    multipart_value = request.form.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
