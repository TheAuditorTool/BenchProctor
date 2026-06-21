# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41030():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
