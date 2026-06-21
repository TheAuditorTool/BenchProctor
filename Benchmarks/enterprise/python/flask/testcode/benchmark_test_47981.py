# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47981():
    ua_value = request.headers.get('User-Agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
