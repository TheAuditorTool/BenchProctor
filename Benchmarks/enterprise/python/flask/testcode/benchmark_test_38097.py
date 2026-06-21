# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38097():
    user_id = request.args.get('id', '')
    data = ' '.join(str(user_id).split())
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
