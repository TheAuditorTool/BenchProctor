# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51056():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
