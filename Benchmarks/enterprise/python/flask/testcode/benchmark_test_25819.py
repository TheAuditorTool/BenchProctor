# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25819():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
