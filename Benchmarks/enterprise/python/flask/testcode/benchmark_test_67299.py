# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67299():
    auth_header = request.headers.get('Authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
