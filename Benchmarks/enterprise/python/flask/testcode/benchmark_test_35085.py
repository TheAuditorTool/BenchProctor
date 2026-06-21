# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35085():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
