# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12645():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value:.200s}'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
