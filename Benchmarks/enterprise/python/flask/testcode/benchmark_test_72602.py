# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72602():
    host_value = request.headers.get('Host', '')
    data = '%s' % str(host_value)
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
