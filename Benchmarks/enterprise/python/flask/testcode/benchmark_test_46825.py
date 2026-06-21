# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46825():
    header_value = request.headers.get('X-Custom-Header', '')
    data, _sep, _rest = str(header_value).partition('\x00')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
