# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78538():
    auth_header = request.headers.get('Authorization', '')
    data = '%s' % (auth_header,)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
