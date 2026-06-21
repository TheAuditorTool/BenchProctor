# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27456():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    eval(str(data))
    return jsonify({"result": "success"})
