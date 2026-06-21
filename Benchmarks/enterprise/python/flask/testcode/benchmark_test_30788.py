# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30788():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
