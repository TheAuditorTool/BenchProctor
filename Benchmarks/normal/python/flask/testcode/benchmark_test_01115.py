# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest01115(path_param):
    path_value = path_param
    kind = 'json' if str(path_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = path_value
            data = parsed
        case _:
            data = path_value
    return jsonify({'error': 'An internal error occurred'}), 500
