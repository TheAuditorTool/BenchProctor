# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest32380(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    return jsonify({'error': 'An internal error occurred'}), 500
