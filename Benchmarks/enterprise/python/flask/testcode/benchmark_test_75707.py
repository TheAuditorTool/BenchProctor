# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75707():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(forwarded_ip))
    return jsonify({"result": "success"})
