# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31488():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
