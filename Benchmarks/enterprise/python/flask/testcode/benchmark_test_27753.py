# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27753():
    origin_value = request.headers.get('Origin', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
