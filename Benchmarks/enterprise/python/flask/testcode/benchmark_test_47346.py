# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47346():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
