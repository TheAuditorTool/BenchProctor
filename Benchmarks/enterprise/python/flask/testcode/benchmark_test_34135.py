# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34135():
    ua_value = request.headers.get('User-Agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    eval(str(data))
    return jsonify({"result": "success"})
