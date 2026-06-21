# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17046():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
