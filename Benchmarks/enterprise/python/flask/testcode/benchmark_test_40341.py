# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest40341(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
