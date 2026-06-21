# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59712():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})
