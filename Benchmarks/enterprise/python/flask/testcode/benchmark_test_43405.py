# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43405():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
