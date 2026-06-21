# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest38473():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
