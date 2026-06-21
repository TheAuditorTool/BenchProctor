# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60733():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
