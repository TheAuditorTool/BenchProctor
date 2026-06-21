# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest17175(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    return jsonify({'error': 'An internal error occurred'}), 500
