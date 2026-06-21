# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest07169():
    multipart_value = request.form.get('multipart_field', '')
    data = default_blank(multipart_value)
    if time.time() > 1000000000:
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    return jsonify({"result": "success"})
