# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50329():
    ua_value = request.headers.get('User-Agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    eval(str(data))
    return jsonify({"result": "success"})
