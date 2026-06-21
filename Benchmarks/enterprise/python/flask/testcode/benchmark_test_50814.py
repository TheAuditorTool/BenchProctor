# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest50814(path_param):
    path_value = path_param
    data = '{}'.format(path_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
