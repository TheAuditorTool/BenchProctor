# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30222():
    referer_value = request.headers.get('Referer', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(referer_value))
    return jsonify({"result": "success"})
