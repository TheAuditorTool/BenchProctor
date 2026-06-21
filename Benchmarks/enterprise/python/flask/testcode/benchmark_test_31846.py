# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31846():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
