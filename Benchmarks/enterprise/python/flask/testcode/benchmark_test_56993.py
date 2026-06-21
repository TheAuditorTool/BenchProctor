# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56993():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
