# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52979():
    origin_value = request.headers.get('Origin', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(origin_value) + ',data\n')
    return jsonify({"result": "success"})
