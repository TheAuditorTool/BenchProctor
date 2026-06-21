# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75878():
    field_value = request.form.get('field', '')
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(field_value))
    return jsonify({"result": "success"})
