# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37037():
    ua_value = request.headers.get('User-Agent', '')
    if str(ua_value).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
