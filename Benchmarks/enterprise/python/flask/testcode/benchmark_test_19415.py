# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19415():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
