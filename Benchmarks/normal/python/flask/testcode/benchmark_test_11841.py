# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11841():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
