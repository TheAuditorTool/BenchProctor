# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def BenchmarkTest03017(path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    return jsonify({'error': 'An internal error occurred'}), 500
