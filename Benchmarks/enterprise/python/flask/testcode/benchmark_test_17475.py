# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17475():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
