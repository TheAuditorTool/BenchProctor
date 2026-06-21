# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest17904(path_param):
    path_value = path_param
    parts = []
    for token in str(path_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
