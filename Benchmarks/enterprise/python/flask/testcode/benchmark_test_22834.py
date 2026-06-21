# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest22834(path_param):
    path_value = path_param
    data = unquote(path_value)
    return jsonify({'error': 'An internal error occurred'}), 500
