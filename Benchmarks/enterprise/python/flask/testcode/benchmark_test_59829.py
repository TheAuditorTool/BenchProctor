# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59829():
    auth_header = request.headers.get('Authorization', '')
    prefix = ''
    data = prefix + str(auth_header)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
