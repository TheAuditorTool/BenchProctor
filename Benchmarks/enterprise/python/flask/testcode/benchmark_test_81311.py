# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest81311():
    auth_header = request.headers.get('Authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
