# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57732():
    host_value = request.headers.get('Host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
