# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69825():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % str(auth_header)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
