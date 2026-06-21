# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10332():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
