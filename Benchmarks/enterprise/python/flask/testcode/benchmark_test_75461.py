# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75461():
    raw_body = request.get_data(as_text=True)
    data = raw_body if raw_body else 'default'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
