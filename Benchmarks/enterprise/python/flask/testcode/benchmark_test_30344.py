# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30344():
    ua_value = request.headers.get('User-Agent', '')
    data = (lambda v: v.strip())(ua_value)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
