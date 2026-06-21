# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68369():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
