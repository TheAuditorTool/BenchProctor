# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest18145(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200
