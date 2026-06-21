# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67630():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value}'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
