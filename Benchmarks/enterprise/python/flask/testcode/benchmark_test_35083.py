# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest35083(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200
