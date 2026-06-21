# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20629():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
