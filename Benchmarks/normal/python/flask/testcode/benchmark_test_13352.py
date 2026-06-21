# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13352():
    origin_value = request.headers.get('Origin', '')
    data = '{}'.format(origin_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
