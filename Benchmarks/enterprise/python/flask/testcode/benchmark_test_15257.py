# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15257():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
