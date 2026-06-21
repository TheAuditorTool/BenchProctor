# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49556():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
