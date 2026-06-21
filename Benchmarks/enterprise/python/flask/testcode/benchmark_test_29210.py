# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session


def BenchmarkTest29210(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500
