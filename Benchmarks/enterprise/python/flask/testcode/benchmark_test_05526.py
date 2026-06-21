# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05526():
    ua_value = request.headers.get('User-Agent', '')
    data = str(ua_value).replace('\x00', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
