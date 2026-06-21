# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest76340():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
