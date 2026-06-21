# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57229():
    ua_value = request.headers.get('User-Agent', '')
    data, _sep, _rest = str(ua_value).partition('\x00')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
