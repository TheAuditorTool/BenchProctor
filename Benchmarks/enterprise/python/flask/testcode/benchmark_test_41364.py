# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41364():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
