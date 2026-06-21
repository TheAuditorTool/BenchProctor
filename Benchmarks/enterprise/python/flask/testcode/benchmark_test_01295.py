# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01295():
    origin_value = request.headers.get('Origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
