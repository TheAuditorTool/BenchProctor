# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52412():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
