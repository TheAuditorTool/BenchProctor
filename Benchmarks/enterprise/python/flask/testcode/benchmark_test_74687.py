# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest74687(path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    return jsonify({'error': 'An internal error occurred'}), 500
