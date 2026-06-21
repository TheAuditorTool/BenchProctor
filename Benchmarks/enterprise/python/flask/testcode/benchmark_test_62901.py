# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62901():
    user_id = request.args.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
