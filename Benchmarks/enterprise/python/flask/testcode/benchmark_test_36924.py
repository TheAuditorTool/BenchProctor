# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session


def BenchmarkTest36924(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
