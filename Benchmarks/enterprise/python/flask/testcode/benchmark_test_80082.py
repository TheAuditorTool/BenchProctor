# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest80082(path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    return jsonify({'error': 'An internal error occurred'}), 500
