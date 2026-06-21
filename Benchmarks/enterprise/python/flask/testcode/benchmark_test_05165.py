# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05165():
    ua_value = request.headers.get('User-Agent', '')
    prefix = ''
    data = prefix + str(ua_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
