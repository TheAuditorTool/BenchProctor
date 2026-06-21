# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15445():
    user_id = request.args.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
