# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11398():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    int(str(data))
    return jsonify({"result": "success"})
