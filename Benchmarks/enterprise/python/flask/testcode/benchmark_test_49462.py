# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49462():
    user_id = request.args.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
