# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time


def to_text(value):
    return str(value).strip()

def BenchmarkTest09194():
    auth_header = request.headers.get('Authorization', '')
    data = to_text(auth_header)
    if time.time() > 1000000000:
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    return jsonify({"result": "success"})
