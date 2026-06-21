# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24736():
    raw_body = request.get_data(as_text=True)
    if raw_body:
        data = raw_body
    else:
        data = ''
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
