# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07129():
    host_value = request.headers.get('Host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
