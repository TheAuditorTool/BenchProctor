# SPDX-License-Identifier: Apache-2.0
import html
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest38020():
    header_value = request.headers.get('X-Custom-Header', '')
    data = relay_value(header_value)
    processed = str(data).replace("<script", "")
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return jsonify({"result": "success"})
