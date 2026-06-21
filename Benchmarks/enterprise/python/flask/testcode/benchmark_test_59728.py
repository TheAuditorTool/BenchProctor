# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59728():
    host_value = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
