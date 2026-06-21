# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11183():
    multipart_value = request.form.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    with open('/var/www/html/exports/report.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})
