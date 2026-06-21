# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05863():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
