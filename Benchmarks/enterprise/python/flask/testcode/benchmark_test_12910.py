# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12910():
    referer_value = request.headers.get('Referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
