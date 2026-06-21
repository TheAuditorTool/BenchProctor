# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest61249(path_param):
    path_value = path_param
    data = unquote(path_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200
