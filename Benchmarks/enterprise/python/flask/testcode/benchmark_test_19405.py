# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19405():
    multipart_value = request.form.get('multipart_field', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(multipart_value))
    return jsonify({"result": "success"})
