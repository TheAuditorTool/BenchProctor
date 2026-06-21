# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80119():
    cookie_value = request.cookies.get('session_token', '')
    if str(cookie_value) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
