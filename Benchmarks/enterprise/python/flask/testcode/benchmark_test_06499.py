# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest06499(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200
