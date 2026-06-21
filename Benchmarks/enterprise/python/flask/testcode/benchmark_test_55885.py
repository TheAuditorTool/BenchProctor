# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55885():
    ua_value = request.headers.get('User-Agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    int(str(data))
    return jsonify({"result": "success"})
