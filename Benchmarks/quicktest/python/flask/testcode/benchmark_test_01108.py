# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01108():
    host_value = request.headers.get('Host', '')
    parts = str(host_value).split(',')
    data = ','.join(parts)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
