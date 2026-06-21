# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest34770(path_param):
    path_value = path_param
    data = normalise_input(path_value)
    return jsonify({'error': 'An internal error occurred'}), 500
