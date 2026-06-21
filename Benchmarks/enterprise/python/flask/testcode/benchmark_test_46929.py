# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46929():
    user_id = request.args.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
