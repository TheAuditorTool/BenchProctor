# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60353():
    ua_value = request.headers.get('User-Agent', '')
    data = str(ua_value).replace('\x00', '')
    eval(str(data))
    return jsonify({"result": "success"})
