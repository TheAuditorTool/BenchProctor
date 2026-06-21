# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest76035(path_param):
    path_value = path_param
    return jsonify({'error': 'An internal error occurred'}), 500
