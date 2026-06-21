# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34986():
    user_id = request.args.get('id', '')
    if str(user_id) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
