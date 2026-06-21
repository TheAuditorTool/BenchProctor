# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37292():
    user_id = request.args.get('id', '')
    data = '{}'.format(user_id)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
