# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14387():
    auth_header = request.headers.get('Authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
