# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45780():
    auth_header = request.headers.get('Authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
