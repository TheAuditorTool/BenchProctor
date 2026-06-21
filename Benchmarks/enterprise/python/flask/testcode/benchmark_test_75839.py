# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75839():
    auth_header = request.headers.get('Authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
