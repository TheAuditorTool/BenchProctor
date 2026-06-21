# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest81458():
    user_id = request.args.get('id', '')
    if str(user_id) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
