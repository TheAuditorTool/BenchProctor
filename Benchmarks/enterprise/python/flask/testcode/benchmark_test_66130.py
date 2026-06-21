# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest66130():
    user_id = request.args.get('id', '')
    data = '%s' % (user_id,)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200
