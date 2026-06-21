# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55237():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
