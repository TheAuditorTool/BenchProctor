# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38321():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
