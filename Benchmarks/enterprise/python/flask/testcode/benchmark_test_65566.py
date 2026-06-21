# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65566():
    host_value = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
