# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41633():
    referer_value = request.headers.get('Referer', '')
    data = (lambda v: v.strip())(referer_value)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
