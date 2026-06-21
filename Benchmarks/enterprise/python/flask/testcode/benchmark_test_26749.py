# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26749():
    referer_value = request.headers.get('Referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
