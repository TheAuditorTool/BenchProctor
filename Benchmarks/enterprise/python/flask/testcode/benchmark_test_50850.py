# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50850():
    auth_header = request.headers.get('Authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
