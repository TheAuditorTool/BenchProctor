# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32326():
    ua_value = request.headers.get('User-Agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
