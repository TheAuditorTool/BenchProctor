# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08588():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
