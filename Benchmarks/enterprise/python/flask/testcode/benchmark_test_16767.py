# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest16767(path_param):
    path_value = path_param
    data = '%s' % (path_value,)
    return jsonify({'error': 'An internal error occurred'}), 500
