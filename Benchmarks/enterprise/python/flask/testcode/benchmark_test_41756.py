# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41756():
    origin_value = request.headers.get('Origin', '')
    data = '{}'.format(origin_value)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
