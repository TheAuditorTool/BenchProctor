# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42450():
    header_value = request.headers.get('X-Custom-Header', '')
    data = str(header_value).replace('\x00', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
