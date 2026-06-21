# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59347():
    header_value = request.headers.get('X-Custom-Header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
