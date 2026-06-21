# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59994():
    origin_value = request.headers.get('Origin', '')
    data = (lambda v: v.strip())(origin_value)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
