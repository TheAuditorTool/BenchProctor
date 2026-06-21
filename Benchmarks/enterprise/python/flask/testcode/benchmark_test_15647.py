# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15647():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip:.200s}'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
