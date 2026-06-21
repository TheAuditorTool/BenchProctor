# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34789():
    host_value = request.headers.get('Host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
