# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49265():
    auth_header = request.headers.get('Authorization', '')
    parts = str(auth_header).split(',')
    data = ','.join(parts)
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})
