# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03631():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body:.200s}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
