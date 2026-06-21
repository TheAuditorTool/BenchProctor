# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75252():
    header_value = request.headers.get('X-Custom-Header', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(header_value) + ',data\n')
    return jsonify({"result": "success"})
