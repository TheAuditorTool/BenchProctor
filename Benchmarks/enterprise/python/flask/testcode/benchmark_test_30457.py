# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest30457(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    return jsonify({'error': 'An internal error occurred'}), 500
