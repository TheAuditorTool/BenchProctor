# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest73382(path_param):
    path_value = path_param
    data = to_text(path_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
