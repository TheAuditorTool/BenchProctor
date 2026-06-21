# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00492():
    ua_value = request.headers.get('User-Agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
