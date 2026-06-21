# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22142():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    if str(data) == 'is_admin':
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
