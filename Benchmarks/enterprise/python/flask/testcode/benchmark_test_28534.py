# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest28534():
    host_value = request.headers.get('Host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
