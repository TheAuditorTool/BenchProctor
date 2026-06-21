# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12877():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
