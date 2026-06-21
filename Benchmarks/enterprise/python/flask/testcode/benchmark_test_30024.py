# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session


def BenchmarkTest30024(path_param):
    path_value = path_param
    parts = str(path_value).split(',')
    data = ','.join(parts)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
