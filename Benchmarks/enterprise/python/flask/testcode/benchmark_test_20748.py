# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20748():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    int(str(data))
    return jsonify({"result": "success"})
