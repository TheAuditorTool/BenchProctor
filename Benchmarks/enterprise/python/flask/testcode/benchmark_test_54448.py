# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54448():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
