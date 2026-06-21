# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31619():
    upload_name = request.files['upload'].filename
    data = f'{upload_name}'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
