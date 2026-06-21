# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54290():
    auth_header = request.headers.get('Authorization', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
