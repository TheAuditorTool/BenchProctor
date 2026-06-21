# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64159():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '{}'.format(header_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
