# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25439():
    origin_value = request.headers.get('Origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
