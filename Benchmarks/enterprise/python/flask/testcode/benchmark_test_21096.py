# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21096():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
