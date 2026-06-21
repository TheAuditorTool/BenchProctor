# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08287():
    host_value = request.headers.get('Host', '')
    data = f'{host_value}'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
