# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68152():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
