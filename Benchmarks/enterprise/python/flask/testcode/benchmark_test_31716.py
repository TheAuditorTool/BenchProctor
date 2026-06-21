# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31716():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return jsonify({"result": "success"})
