# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01798():
    host_value = request.headers.get('Host', '')
    data = '{}'.format(host_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
