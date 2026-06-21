# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58014():
    raw_body = request.get_data(as_text=True)
    data = ' '.join(str(raw_body).split())
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
