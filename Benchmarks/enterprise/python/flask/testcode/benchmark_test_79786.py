# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79786():
    user_id = request.args.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
