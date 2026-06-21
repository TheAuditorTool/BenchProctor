# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52928():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
