# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21531():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
