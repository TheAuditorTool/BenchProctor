# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest27059():
    auth_header = request.headers.get('Authorization', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(auth_header))
    return jsonify({"result": "success"})
