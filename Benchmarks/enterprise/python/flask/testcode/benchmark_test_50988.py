# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50988():
    raw_body = request.get_data(as_text=True)
    data, _sep, _rest = str(raw_body).partition('\x00')
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
