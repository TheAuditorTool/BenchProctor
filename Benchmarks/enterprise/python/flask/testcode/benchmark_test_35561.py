# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35561():
    multipart_value = request.form.get('multipart_field', '')
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(multipart_value))
    return jsonify({"result": "success"})
