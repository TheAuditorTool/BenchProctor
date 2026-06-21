# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest67399():
    cookie_value = request.cookies.get('session_token', '')
    data = coalesce_blank(cookie_value)
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})
