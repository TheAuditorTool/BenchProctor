# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest32630(path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    return jsonify({'error': 'An internal error occurred'}), 500
