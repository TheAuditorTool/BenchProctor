# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session


def BenchmarkTest14602(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
