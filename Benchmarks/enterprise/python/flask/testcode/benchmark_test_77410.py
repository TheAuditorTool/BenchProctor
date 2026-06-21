# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77410():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
