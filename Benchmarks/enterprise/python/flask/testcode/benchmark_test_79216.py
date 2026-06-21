# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79216():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
