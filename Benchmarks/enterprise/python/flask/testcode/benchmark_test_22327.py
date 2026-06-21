# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22327():
    host_value = request.headers.get('Host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    eval(str(data))
    return jsonify({"result": "success"})
