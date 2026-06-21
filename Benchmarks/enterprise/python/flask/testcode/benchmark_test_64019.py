# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64019():
    host_value = request.headers.get('Host', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(host_value))
    return jsonify({"result": "success"})
