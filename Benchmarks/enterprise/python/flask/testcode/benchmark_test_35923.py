# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35923():
    origin_value = request.headers.get('Origin', '')
    data = str(origin_value).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
