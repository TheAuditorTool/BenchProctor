# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest29367(path_param):
    path_value = path_param
    return jsonify({'error': 'An internal error occurred'}), 500
