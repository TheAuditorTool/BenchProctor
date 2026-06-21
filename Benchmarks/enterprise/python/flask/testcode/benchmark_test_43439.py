# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43439():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200
