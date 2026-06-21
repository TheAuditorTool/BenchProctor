# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09165():
    header_value = request.headers.get('X-Custom-Header', '')
    data = str(header_value).replace('\x00', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
