# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27062():
    auth_header = request.headers.get('Authorization', '')
    data = str(auth_header).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
