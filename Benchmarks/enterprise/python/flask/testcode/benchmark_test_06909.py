# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest06909(path_param):
    path_value = path_param
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500
