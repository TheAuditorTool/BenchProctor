# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22574():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200
