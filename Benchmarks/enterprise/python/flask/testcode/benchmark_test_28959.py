# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28959():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
