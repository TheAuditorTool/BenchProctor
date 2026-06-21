# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33339():
    user_id = request.args.get('id', '')
    data = user_id if user_id else 'default'
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
