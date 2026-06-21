# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02465():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
