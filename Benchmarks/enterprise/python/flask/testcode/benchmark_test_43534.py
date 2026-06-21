# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43534():
    host_value = request.headers.get('Host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    int(str(data))
    return jsonify({"result": "success"})
