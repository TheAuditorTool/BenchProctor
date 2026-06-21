# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02922():
    ua_value = request.headers.get('User-Agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
