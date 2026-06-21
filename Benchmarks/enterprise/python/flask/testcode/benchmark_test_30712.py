# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30712():
    auth_header = request.headers.get('Authorization', '')
    if str(auth_header) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
