# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32724():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
