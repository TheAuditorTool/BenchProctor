# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time


def coalesce_blank(value):
    return value or ''

def BenchmarkTest13897():
    user_id = request.args.get('id', '')
    data = coalesce_blank(user_id)
    if time.time() > 1000000000:
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    return jsonify({"result": "success"})
