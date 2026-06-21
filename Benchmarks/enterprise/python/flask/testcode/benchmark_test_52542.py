# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52542():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})
