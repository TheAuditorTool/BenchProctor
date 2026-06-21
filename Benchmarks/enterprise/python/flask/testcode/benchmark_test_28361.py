# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28361():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
