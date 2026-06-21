# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47206():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
