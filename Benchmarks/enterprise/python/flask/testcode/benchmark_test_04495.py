# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04495():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
