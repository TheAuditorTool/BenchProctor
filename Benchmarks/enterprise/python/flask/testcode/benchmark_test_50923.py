# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50923():
    user_id = request.args.get('id', '')
    data = '{}'.format(user_id)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
