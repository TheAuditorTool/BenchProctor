# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest44504():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
