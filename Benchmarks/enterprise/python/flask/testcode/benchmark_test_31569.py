# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31569():
    user_id = request.args.get('id', '')
    data = str(user_id).replace('\x00', '')
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
