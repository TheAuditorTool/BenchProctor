# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest46165(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    return jsonify({'error': 'An internal error occurred'}), 500
