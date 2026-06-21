# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56825():
    origin_value = request.headers.get('Origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
