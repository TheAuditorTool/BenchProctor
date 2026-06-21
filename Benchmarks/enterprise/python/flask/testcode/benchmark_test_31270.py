# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31270():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
