# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03991():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
