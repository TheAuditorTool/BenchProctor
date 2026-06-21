# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53875():
    origin_value = request.headers.get('Origin', '')
    if str(origin_value) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
