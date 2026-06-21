# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31712():
    host_value = request.headers.get('Host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
