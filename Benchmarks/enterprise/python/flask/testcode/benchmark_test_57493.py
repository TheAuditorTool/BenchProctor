# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest57493():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
