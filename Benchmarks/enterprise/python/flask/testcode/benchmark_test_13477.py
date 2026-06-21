# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13477():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '%s' % str(forwarded_ip)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
