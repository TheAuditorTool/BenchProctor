# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest59655():
    referer_value = request.headers.get('Referer', '')
    data, _sep, _rest = str(referer_value).partition('\x00')
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
