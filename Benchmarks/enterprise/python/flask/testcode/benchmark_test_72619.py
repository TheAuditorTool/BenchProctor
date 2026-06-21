# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72619():
    raw_body = request.get_data(as_text=True)
    data = (lambda v: v.strip())(raw_body)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200
