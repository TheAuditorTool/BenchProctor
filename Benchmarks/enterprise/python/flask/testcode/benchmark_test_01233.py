# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest01233():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
